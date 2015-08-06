from flask import Flask

app = Flask(__name__)

# import routes
import routes.app_routes
import routes.default_routes
import routes.keys_routes
import routes.media_routes
