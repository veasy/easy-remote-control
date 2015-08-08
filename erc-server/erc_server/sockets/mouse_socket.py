from erc_server import Xdotool
from erc_server import socketio
from flask.ext.socketio import emit
from erc_server.unified_control.mouse import unified_mouse

__author__ = 'cansik'

MOUSE_NAMESPACE = '/mouse'

@socketio.on('connect', namespace=MOUSE_NAMESPACE)
def mouse_connect():
    print('Client connected')

@socketio.on('mouseDragged', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
    dx = int(message['x'])
    dy = int(message['y'])
    unified_mouse.move_mouse_relate(dx, dy)
    #Xdotool.mousemove_relate(dx, dy)
    print message

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
