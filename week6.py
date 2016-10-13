import ConfigParser

from flask import Flask, session, flash, redirect, request, url_for, render_template

app=Flask(__name__)
app.secret_key = 'AOZr(*j/3kyX RuXHH!jmN]LWX/,?RT'

@app.route('/')
def index():
  return render_template('index.html')

  return "Root Page"

@app.route('/config/')
def config():
  str=[]
  str.append('debug:'+app.config['DEBUG'])
  str.append('port'+app.config['port'])
  str.append('url'+app.config['url'])
  str.append('ip_adress'+app.config['ip_adress'])
  return '\t'.join(str)

def init(app):
  config=ConfigParser.ConfigParser()
  try:
    config_location="etc/defaults.cfg"
    config.read(config_location)

    app.config['DEBUG']=config.get("config","debug")
    app.config['ip_adress']=config.get("config","ip_adress")
    app.config['port']=config.get("config","port")
    app.config['url']=config.get("config","url")
  except:
    print"Could not reqd configs from :", config_location

@app.route('/session/write/<name>/')
def write(name=None):
  session['name']=name
  return "Wrote %s into 'name' key of session" % name

@app.route('/session/read/')
def read():
  try:
    if(session['name']):
      return str(session['name'])
  except KeyError:
    pass
  return "Net session variable set for 'name' key'"

@app.route('/session/remove/')
def remove():
  session.pop('name',None)
  return "Removed key 'name' from session"

@app.route('/login/<message>')
def login(message):
  if(message!=None):
    flash(message)
  flash("A default message")
  return "Let's pretend you just logged in"

if __name__=='__main__':
  init(app)
  app.run(
    host=app.config['ip_adress'],
    port=int(app.config['port']))
