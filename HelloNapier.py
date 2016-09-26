from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/apple')
def static_example_img():
  start = '<img src="'
  url = url_for('static', filename='apple.jpg')
  end='">'
  return start+url+end, 200

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
