from flask import Flask
from flask.ext.socketio import SocketIO
from flask.ext.cors import CORS

import erc_config

app = Flask(__name__,
            static_folder=erc_config.ERC_SERVER_STATIC_FOLDER,
            static_url_path=erc_config.ERC_SERVER_STATIC_PATH,
            template_folder=erc_config.ERC_SERVER_TEMPLATE_FOLDER)

app.config['SECRET_KEY'] = 'secret!'

CORS(app)

socketio = SocketIO(app)

# import routes
import routes.app_routes
import routes.default_routes
import routes.keys_routes
import routes.media_routes
import sockets.mouse_socket
