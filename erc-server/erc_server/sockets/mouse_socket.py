from pyunicon.UCScreen import UCScreen
from erc_server import socketio
from flask.ext.socketio import emit
from pyunicon.UCMouse import UCMouse

__author__ = 'cansik'

DEFAULT_NAMESPACE = '/mouse'

__mouse = UCMouse()
__screen = UCScreen()


@socketio.on('connect', namespace=DEFAULT_NAMESPACE)
def mouse_connect():
    print('Client connected')


@socketio.on('mouseDragged', namespace=DEFAULT_NAMESPACE)
def mouse_message(message):
    dx = float(message['x'])
    dy = float(message['y'])

    width, height = __screen.get_size()

    dx = (dx / 640) * width
    dy = (dy / 640) * height

    __mouse.move_relative(dx, dy)


@socketio.on('mouseLeft', namespace=DEFAULT_NAMESPACE)
def mouse_message(message):
    __mouse.click_left()
    print 'left click'


@socketio.on('mouseRight', namespace=DEFAULT_NAMESPACE)
def mouse_message(message):
    __mouse.click_right()
    print 'right click'


@socketio.on('disconnect', namespace=DEFAULT_NAMESPACE)
def mouse_disconnect():
    print('Client disconnected')
