import Xdotool
from erc_server import socketio
from flask.ext.socketio import emit

__author__ = 'cansik'

MOUSE_NAMESPACE = '/mouse'

@socketio.on('connect', namespace=MOUSE_NAMESPACE)
def mouse_connect():
    print('Client connected')

@socketio.on('mouseDragged', namespace=MOUSE_NAMESPACE)
def mouse_message(message):

    dx = int(message['data']['x'])
    dy = int(message['data']['y'])
    Xdotool.mousemove_relate(dx, dy)

    #coordinates = Xdotool.getmouselocation()
    #x = int(coordinates['x']) + dx
    #y = int(coordinates['y']) + dy

    #Xdotool.mousemove(x, y)
    print message

@socketio.on('mouseLeft', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
    print message

@socketio.on('mouseRight', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
    print message

@socketio.on('disconnect', namespace=MOUSE_NAMESPACE)
def mouse_disconnect():
    print('Client disconnected')
