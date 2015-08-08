from unified_control.mouse import x_mouse

__author__ = 'cansik'

# todo: change behavor on os type
mouse = x_mouse

def move_mouse(x, y):
    mouse.move_mouse(x, y)
