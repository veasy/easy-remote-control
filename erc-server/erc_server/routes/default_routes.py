from flask import render_template
from erc_server import app


@app.route('/')
def root():
    return render_template('index.html')