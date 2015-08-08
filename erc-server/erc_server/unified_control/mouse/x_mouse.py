from ctypes import cdll


def move_mouse(x, y):
    dll = cdll.LoadLibrary('libX11.so')
    d = dll.XOpenDisplay(None)
    root = dll.XDefaultRootWindow(d)
    dll.XWarpPointer(d, None, root, 0, 0, 0, 0, x, y)
    dll.XCloseDisplay(d)


def move_mouse_relative(dx, dy):
    x, y = get_mouse_position()
    move_mouse(abs(x + dx), abs(y + dy))
    pass


def get_mouse_position():
    dll = cdll.LoadLibrary('libX11.so')
    d = dll.XOpenDisplay(None)
    root = dll.XDefaultRootWindow(d)
    # todo: do somethinghere
    x = 0
    y = 0
    result = dll.XQueryPointer(d, root, 0, 0, 0, 0, x, y, 0)

    print 'Result: %s' % result
    print 'Coordinates: %s, %s' % (x, y)

    dll.XCloseDisplay(d)
    return x, y
