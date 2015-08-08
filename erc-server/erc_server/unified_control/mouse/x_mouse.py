from ctypes import cdll


def move_mouse(x, y):
    dll = cdll.LoadLibrary('libX11.so')
    d = dll.XOpenDisplay(None)
    root = dll.XDefaultRootWindow(d)
    dll.XWarpPointer(d, None, root, 0, 0, 0, 0, x, y)
    dll.XCloseDisplay(d)
