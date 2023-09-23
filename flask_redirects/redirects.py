from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/private")
def private():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "now we would get username and password"

@app.route("/force404")
def force404():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you were looking for"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
