import subprocess

__author__ = 'cansik'


def mousemove(x, y):
    output = __xdotool_call('mousemove %s %s' % (x, y))
    print output
    pass

def mousemove_relate(dx, dy):
    __xdotool_call('mousemove_relative -- %s %s' % (dx, dy))

def click(direction):
    __xdotool_call('click %s' % direction)

def getmouselocation():
    result = __xdotool_call('getmouselocation')
    coordinates = dict([x.split(':') for x in result.split(' ')])
    return coordinates


def __xdotool_call(command):
    output = subprocess.check_output('xdotool %s' % command, shell=True)
    return output.strip()
