from pyunicon.util import UCKey
from erc_server import app
from erc_server.erc_util import press_key

__author__ = 'cansik'

ROUTE_PATH = '/keys'


# -------- arrows --------
@app.route('%s/up' % ROUTE_PATH)
def route_keys_up():
    return press_key(UCKey.UC_UP)


@app.route('%s/down' % ROUTE_PATH)
def route_keys_down():
    return press_key(UCKey.UC_DOWN)


@app.route('%s/left' % ROUTE_PATH)
def route_keys_left():
    return press_key(UCKey.UC_LEFT)


@app.route('%s/right' % ROUTE_PATH)
def route_keys_right():
    return press_key(UCKey.UC_RIGHT)


# -------- default --------
@app.route('%s/escape' % ROUTE_PATH)
def route_keys_escape():
    return press_key(UCKey.UC_ESCAPE)


@app.route('%s/return' % ROUTE_PATH)
def route_keys_return():
    return press_key(UCKey.UC_RETURN)
