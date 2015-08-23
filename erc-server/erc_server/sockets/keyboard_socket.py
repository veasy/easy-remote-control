from pyunicon.UCScreen import UCScreen
from erc_server import socketio
from flask.ext.socketio import emit
from pyunicon.UCMouse import UCMouse
from erc_server.erc_util import get_key_by_text, press_key

__author__ = 'cansik'

DEFAULT_NAMESPACE = '/text'

__mouse = UCMouse()
__screen = UCScreen()


@socketio.on('connect', namespace=DEFAULT_NAMESPACE)
def connect():
    print('Client connected')


@socketio.on('char', namespace=DEFAULT_NAMESPACE)
def char(key):
    key_code = get_key_by_text(key.upper())
    press_key(key_code)
    print 'Received char: %s' % key


@socketio.on('disconnect', namespace=DEFAULT_NAMESPACE)
def disconnect():
    print('Client disconnected')
