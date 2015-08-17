import os
import flask
from pyunicon.UCKeyboard import UCKeyboard

__author__ = 'cansik'

__keyboard = UCKeyboard()

def press_key(key):
    code = 0
    __keyboard.send_key(key)
    return flask.jsonify({'key': key, 'code': code})