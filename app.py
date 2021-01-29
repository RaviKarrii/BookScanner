from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/twopage',methods=['POST'])
def twopage():
    if request.method == 'POST':
        for i in request.files.getlist('file'):
            i.save(os.path.join("tmp/",secure_filename(i.filename)))
    return 'file uploaded successfully'

if __name__ == '__main__':
    app.run()