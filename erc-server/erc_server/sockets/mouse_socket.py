from erc_server import socketio
from flask.ext.socketio import emit
from flask.ext.cors import cross_origin

__author__ = 'cansik'

MOUSE_NAMESPACE = '/mouse'

@socketio.on('connect', namespace=MOUSE_NAMESPACE)
def mouse_connect():
    print('Client connected')
    emit('hello', {'data': 'Hello Markus, you are Connected'})

@socketio.on('mouse moved', namespace=MOUSE_NAMESPACE)
def mouse_message(message):
    print message

@socketio.on('disconnect', namespace=MOUSE_NAMESPACE)
def mouse_disconnect():
    print('Client disconnected')
