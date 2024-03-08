from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """return a friendly greeting."""
    print("I am inside hello world")
    return 'hello world! ccf-gcp is working!'


@app.route('/echo/<name>')
def echo(name):
    print(f"This is placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == '__main__':
    # checks for app.yaml before running
    import os
    if os.path.exists("app.yaml"):
        app.run(host='127.0.0.1', port=8080, debug=True)
    else:
        print("app.yaml not found!")
