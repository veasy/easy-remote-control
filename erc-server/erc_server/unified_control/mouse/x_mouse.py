from ctypes import *

# custom types
t_Atom = c_ulong
t_Bool = c_int
t_Display = c_void_p
t_Window = c_ulong
t_Colormap = c_ulong

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
    xwa = _get_xwindow_attributes()
    return int(xwa.width), int(xwa.height)


def _get_xwindow_attributes():
    xwa = XWindowAttributes()
    _xlib.XGetWindowAttributes(_display, _window, byref(xwa))
    return xwa


class XWindowAttributes(Structure):
    _fields_ = [
        ('x', c_int),
        ('y', c_int),
        ('width', c_int),
        ('height', c_int),
        ('border_width', c_int),
        ('depth', c_int),
        ('visual', c_void_p),
        ('root', t_Window),
        ('class', c_int),
        ('bit_gravity', c_int),
        ('win_gravity', c_int),
        ('backing_store', c_int),
        ('backing_planes', c_ulong),
        ('backing_pixel', c_ulong),
        ('save_under', t_Bool),
        ('colormap', t_Colormap),
        ('map_installed', t_Bool),
        ('map_state', c_int),
        ('all_event_masks', c_long),
        ('your_event_masks', c_long),
        ('do_not_propagate_mask', c_long),
        ('override_redirect', t_Bool),
        ('screen', c_void_p),
    ]
