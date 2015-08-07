import erc_config
from erc_server import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=erc_config.ERC_SERVER_PORT,
            debug=erc_config.ERC_SERVER_DEBUG_MODE)
