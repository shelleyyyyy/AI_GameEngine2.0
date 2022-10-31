from flask import Flask

app = Flask(__name__)

@app.route("/data")
def run_sim():
    return "<p>Hello, World!</p>"