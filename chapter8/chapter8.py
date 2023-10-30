import configparser

from flask import Flask, session, flash, redirect, request, url_for, render_template
app = Flask(__name__)
app.secret_key = 'AOZr98j/3yX R#~XHH!jmN]LWX/,?RT'

def init(app):
    config = configparser.ConfigParser()
    try:
        print("INIT FUNCTION")
        config_location = "etc/defaults.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
    except:
        print("could not read configs from:" , config_location)

init(app)

@app.route('/')
def root():
    return "hello from config testing app"

@app.route('/config/')
def config():
    s = []
    s.append('debug:'+str(app.config['DEBUG']))
    s.append('port:'+app.config['port'])
    s.append('url:'+app.config['url'])
    s.append('ip_address:'+app.config['ip_address'])
    return ', '.join(s)

@app.route('/sessions/write/<name>/')
def write(name=None):
    session['name'] = name
    return "Wrote %s into 'name key of session" % name

@app.route('/sessions/read/')
def read():
    try:
        if(session['name']):
            return str(session['name'])
    except KeyError:
        pass
    return "No session variable set for 'name' key"

@app.route('/session/remove/')
def romve():
    session.pop('name', None)
    return "removed key 'name from session"

@app.route('/flash/')
def index():
    return render_template('index.html')

@app.route('/login/')
@app.route('/login/<message>')
def login(message=None):
    if(message!=None):
        flash(message)
    else:
        flash(u'Default message')
    return redirect(url_for('index'))

if __name__ =='__main__':
    init(app)
    app.run(
        host=app.config['ip_address'],
        port=int(app.config['port']))
