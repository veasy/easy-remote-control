from erc_server import socketio
from flask.ext.socketio import emit

__author__ = 'cansik'

MOUSE_NAMESPACE = '/mouse'

@socketio.on('connect', namespace=MOUSE_NAMESPACE)
def mouse_connect():
    print('Client connected')

@socketio.on('mouseDragged', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
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
