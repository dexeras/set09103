from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  print request.method, request.path, request.form
  return request.method+request.path+"Hello World!"

@app.route('/apple')
def static_example_img():
  start = '<img src="'
  url = url_for('static', filename='apple.jpg')
  end='">'
  return start+url+end, 200

@app.route("/account/", methods=['POST','GET'])
def account():
  if request.method=='POST':
    print request.form
    name = request.form['name']
    return request.method+request.path+"Hello %s" % name
  else:
    page='''
    <html><body>
      <form action="" method="post" name="form">
        <label for="name">Name : </label>
        <input type="text" name = "name" id="name"/>
        <input type="submit" nqme="submit" id="submit"/>
      </form>
    </body></html>'''
    return request.method+request.path+page

@app.route("/hello/")
def helloname():
  name = request.args.get('name','')
  if name == '':
    return'''Hello stranger, give me your name by typing it as an encoded
    parameter in the URL ;)'''
  else:
    return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first,second):
  return str(first+second)

@app.route("/upload/", methods=['POST','GET'])
def upload():
  if request.method=="POST":
    f=request.files['datafile']
    f.save('static/uploads/file.png')
    return "File uploaded"
  else:
    page='''
    <html><body>
    <form action="" method="post" name="form" enctype="multipart/form-data">
    <input type="file" name="datafile" />
    <input type="submit" name="submit" id="submit"/>
    </form></body></html>
    '''
    return page, 200


@app.route("/hello/<name>")
def helloTemplate(name=None):
  user={'name':name}
  return render_template('hello.html',user=user)

@app.route("/conditional/")
@app.route("/conditional/<name>")
def conditional(name=None):
  return render_template('conditional.html',name=name)

@app.route('/users/')
def users():
  names=['axel','alex','bastien','yohan','damien','bertine','benoit']
  return render_template('loop.html',names=names)

@app.route('/inherits/')
def inherits():
  return render_template('inheritance.html')

@app.route('/inherits/one')
def inherits_one():
  return render_template('content1.html')

@app.route('/inherits/two')
def inherits_two():
  return render_template('content2.html')


@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
