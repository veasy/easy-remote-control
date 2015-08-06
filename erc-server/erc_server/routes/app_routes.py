__author__ = 'cansik'

from erc_server import app

ROUTE_PATH = '/app/<app_name>'


@app.route('%s/focus' % ROUTE_PATH)
def route_app_focus(app_name):
    return 'focus %s' % app_name


@app.route('%s/start' % ROUTE_PATH)
def route_app_start(app_name):
    return 'start %s' % app_name


@app.route('%s/stop' % ROUTE_PATH)
def route_app_stop(app_name):
    return 'stop %s' % app_name