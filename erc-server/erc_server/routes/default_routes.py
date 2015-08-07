from flask import render_template
import erc_config
from erc_server import app


@app.route('/')
def root():
    return render_template('index.html', resources=erc_config.ERC_SERVER_STATIC_PATH)