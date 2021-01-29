from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/twopage')
def twopage():
    if request.method == 'POST':
        f = request.files.getlist("file")
        for i in f:
            try:
                i.save(os.path.join("/tmp/",secure_filename(i.filename)))
            except e:
                return e
    return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()