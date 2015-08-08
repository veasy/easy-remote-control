import os

__author__ = 'cansik'


def mousemove(x, y):
    __xdotool_call('mousemove %s %s' % (x, y))
    pass


def getmouselocation():
    # x:418 y:420 screen:0 window:417
    result = __xdotool_call('getmouselocation')
    return result


def __xdotool_call(command):
    code = os.system('xdotool %s' % command)
    return code
