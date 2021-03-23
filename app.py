import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Yo whats up! How is it going:D!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
