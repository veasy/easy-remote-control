from _ctypes import byref
from ctypes import cdll, c_uint32, c_int, c_uint

_xlib = cdll.LoadLibrary('libX11.so')
_display = _xlib.XOpenDisplay(None)
_window = _xlib.XDefaultRootWindow(_display)

def close_display():
    _xlib.XCloseDisplay(_display)

def move_mouse(x, y):
    _xlib.XWarpPointer(_display, None, _window, 0, 0, 0, 0, int(x), int(y))


def move_mouse_relative(dx, dy):
    x, y = get_mouse_position()
    move_mouse(x.value + dx, y.value + dy)
    pass


def get_mouse_position():
    (root_id, child_id) = (c_uint32(), c_uint32())
    (root_x, root_y, win_x, win_y) = (c_int(), c_int(), c_int(), c_int())
    mask = c_uint()
    _xlib.XQueryPointer(_display, c_uint32(_window), byref(root_id), byref(child_id),
                        byref(root_x), byref(root_y),
                        byref(win_x), byref(win_y), byref(mask))

    # print 'Result: %s' % result
    # print 'Coordinates: %s, %s' % (root_x, root_y)

    return root_x, root_y

def get_screen_size():
    attributes = _xlib.XWindowAttributes()
    _xlib.XGetWindowAttributes(_display, _window, byref(attributes))
    print '--> attributes: %s' % attributes
    return attributes.root
