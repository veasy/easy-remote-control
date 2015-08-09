from sys import platform as _platform

__author__ = 'cansik'

__mouse = None

# todo: change behaviour on os type
if _platform == "linux" or _platform == "linux2":
    from erc_server.unified_control.mouse import x_mouse
    __mouse = x_mouse

elif _platform == "darwin":
    print('osx is not support atm!')

elif _platform == "win32":
    print('windows is not supported atm!')


def move_mouse(x, y):
    __mouse.move_mouse(x, y)


def move_mouse_relate(dx, dy):
    __mouse.move_mouse_relative(dx, dy)


def get_mouse_position():
    return __mouse.get_mouse_position()


def get_screen_size():
    return __mouse.get_screen_size()
