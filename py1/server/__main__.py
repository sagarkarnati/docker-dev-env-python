from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Great its working, as expected"


if __name__ == '__main__':
    port = os.environ['PORT']
    app.run(host='0.0.0.0', port=port)
