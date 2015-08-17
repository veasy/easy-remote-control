from pyunicon.util.UCKeyCode import UCKeyCode
from erc_server import app
from erc_server.erc_util import press_key

__author__ = 'cansik'

ROUTE_PATH = '/media'
VOLUME_ROUTE_PATH = '%s/volume' % ROUTE_PATH


@app.route('%s/play' % ROUTE_PATH)
def route_volume_play():
    return press_key(UCKeyCode('XF86AudioPlay', None, None, None))


@app.route('%s/next' % ROUTE_PATH)
def route_volume_next():
    return press_key(UCKeyCode('XF86AudioNext', None, None, None))


@app.route('%s/previous' % ROUTE_PATH)
def route_volume_previous():
    return press_key(UCKeyCode('XF86AudioPrev', None, None, None))


@app.route('%s/up' % VOLUME_ROUTE_PATH)
def route_volume_up():
    return press_key(UCKeyCode('XF86AudioLowerVolume', None, None, None))


@app.route('%s/down' % VOLUME_ROUTE_PATH)
def route_volume_down():
    return press_key(UCKeyCode('XF86AudioRaiseVolume', None, None, None))


@app.route('%s/mute' % VOLUME_ROUTE_PATH)
def route_volume_mute():
    return press_key(UCKeyCode('XF86AudioMute', None, None, None))
