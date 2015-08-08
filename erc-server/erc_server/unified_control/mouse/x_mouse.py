from _ctypes import byref
from ctypes import cdll, c_uint32, c_int, c_uint


def move_mouse(x, y):
    dll = cdll.LoadLibrary('libX11.so')
    d = dll.XOpenDisplay(None)
    root = dll.XDefaultRootWindow(d)
    dll.XWarpPointer(d, None, root, 0, 0, 0, 0, x, y)
    dll.XCloseDisplay(d)


def move_mouse_relative(dx, dy):
    x, y = get_mouse_position()
    move_mouse(abs(x.value + dx), abs(y.value + dy))
    pass


def get_mouse_position():
    dll = cdll.LoadLibrary('libX11.so')
    d = dll.XOpenDisplay(None)
    w = dll.XDefaultRootWindow(d)
    # todo: do somethinghere
    (root_id, child_id) = (c_uint32(), c_uint32())
    (root_x, root_y, win_x, win_y) = (c_int(), c_int(), c_int(), c_int())
    mask = c_uint()
    result = dll.XQueryPointer(d, c_uint32(w), byref(root_id), byref(child_id),
                               byref(root_x), byref(root_y),
                               byref(win_x), byref(win_y), byref(mask))

    print 'Result: %s' % result
    print 'Coordinates: %s, %s' % (root_x, root_y)

    dll.XCloseDisplay(d)
    return root_x, root_y
