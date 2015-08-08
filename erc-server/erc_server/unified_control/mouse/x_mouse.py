from _ctypes import byref
from ctypes import cdll, c_uint32, c_int, c_uint

xlib = cdll.LoadLibrary('libX11.so')
d = xlib.XOpenDisplay(None)
w = xlib.XDefaultRootWindow(d)

def move_mouse(x, y):
    xlib.XWarpPointer(d, None, w, 0, 0, 0, 0, int(x), int(y))


def move_mouse_relative(dx, dy):
    x, y = get_mouse_position()
    move_mouse(x.value + dx, y.value + dy)
    pass


def get_mouse_position():
    (root_id, child_id) = (c_uint32(), c_uint32())
    (root_x, root_y, win_x, win_y) = (c_int(), c_int(), c_int(), c_int())
    mask = c_uint()
    xlib.XQueryPointer(d, c_uint32(w), byref(root_id), byref(child_id),
                      byref(root_x), byref(root_y),
                      byref(win_x), byref(win_y), byref(mask))

    # print 'Result: %s' % result
    # print 'Coordinates: %s, %s' % (root_x, root_y)

    return root_x, root_y

def close_display():
    xlib.XCloseDisplay(d)
