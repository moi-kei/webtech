from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return "The default, root, route"

@app.route("/hello/")
def hello():
    return 'hello world'

@app.route("/goodbye/")
def goodbye():
    return "goodbye cruel world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
