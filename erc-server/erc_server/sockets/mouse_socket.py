import autopy
from erc_server import Xdotool
from erc_server import socketio
from flask.ext.socketio import emit
import math

__author__ = 'cansik'

MOUSE_NAMESPACE = '/mouse'

@socketio.on('connect', namespace=MOUSE_NAMESPACE)
def mouse_connect():
    print('Client connected')

@socketio.on('mouseDragged', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
    dx = float(message['x'])
    dy = float(message['y'])

    width, height = autopy.screen.get_size()
    cx, cy = autopy.mouse.get_pos()

    x = int(dx + float(cx))
    y = int(dy + float(cy))

    # check bounds
    x = min(width - 1, max(0, x))
    y = min(height - 1, max(0, y))

    autopy.mouse.move(x, y)

@socketio.on('mouseLeft', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
    Xdotool.click(1)
    print 'left click'

@socketio.on('mouseRight', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
    Xdotool.click(3)
    print 'right click'

@socketio.on('disconnect', namespace=MOUSE_NAMESPACE)
def mouse_disconnect():
    print('Client disconnected')
