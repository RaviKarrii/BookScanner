from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/twopage')
def twopage():
    if request.method == 'POST':
      f = request.files[getlist("file")
      for i in f:
        i.save(secure_filename(i.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = "/tmp/"
    app.run()