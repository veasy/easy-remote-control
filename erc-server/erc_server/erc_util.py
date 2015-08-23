import os
import flask
from pyunicon.UCKeyboard import UCKeyboard
from pyunicon.util import UCKey

__author__ = 'cansik'

__keyboard = UCKeyboard()


def press_key(key):
    code = 0
    __keyboard.send_key(key)
    # flask.jsonify({'key': key, 'code': code})
    return "OK"


def get_key_by_text(text):
    # todo: fix this with a nice solution
    return eval('UCKey.UC_%s' % text)

