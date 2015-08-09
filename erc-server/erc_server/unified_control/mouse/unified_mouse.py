from erc_server.unified_control.mouse import x_mouse

__author__ = 'cansik'

# todo: change behaviour on os type
__mouse = x_mouse

def move_mouse(x, y):
    __mouse.move_mouse(x, y)

def move_mouse_relate(dx, dy):
    __mouse.move_mouse_relative(dx, dy)

def get_mouse_position():
    return __mouse.get_mouse_position()

def get_screen_size():
    return __mouse.get_screen_size()