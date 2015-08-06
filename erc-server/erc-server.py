from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/up")
def up():
    os.system("xdotool key Up")
    return "up clicked"

@app.route("/down")
def down():
    os.system("xdotool key Down")
    return "down clicked"

@app.route("/left")
def left():
    os.system("xdotool key Left")
    return "left clicked"

@app.route("/right")
def right():
    os.system("xdotool key Right")
    return "right clicked"

@app.route("/play")
def play():
    os.system("xdotool key Return")
    return "enter clicked"

@app.route("/menu")
def menu():
    os.system("xdotool key Escape")
    return "menu clicked"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
