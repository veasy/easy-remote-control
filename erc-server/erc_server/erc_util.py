import os
import flask

__author__ = 'cansik'


def press_key(key):
    code = os.system('xdotool key %s' % key)
    return flask.jsonify({'key': key, 'code': code})
