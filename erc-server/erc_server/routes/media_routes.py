from erc_server import app
from erc_server.erc_util import press_key

__author__ = 'cansik'

ROUTE_PATH = '/media'
VOLUME_ROUTE_PATH = '%s/volume' % ROUTE_PATH


@app.route('%s/play' % ROUTE_PATH)
def route_volume_play():
    return press_key('XF86AudioPlay')


@app.route('%s/next' % ROUTE_PATH)
def route_volume_next():
    return press_key('XF86AudioNext')


@app.route('%s/previous' % ROUTE_PATH)
def route_volume_previous():
    return press_key('XF86AudioPrev')


@app.route('%s/up' % VOLUME_ROUTE_PATH)
def route_volume_up():
    return press_key('XF86AudioLowerVolume')


@app.route('%s/down' % VOLUME_ROUTE_PATH)
def route_volume_down():
    return press_key('XF86AudioRaiseVolume')


@app.route('%s/mute' % VOLUME_ROUTE_PATH)
def route_volume_mute():
    return press_key('XF86AudioMute')
