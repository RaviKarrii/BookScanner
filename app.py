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
            i.save(os.path.join("/tmp/",secure_filename(i.filename)))
    return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()