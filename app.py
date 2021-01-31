from flask import Flask, render_template, request,send_file
from werkzeug.utils import secure_filename
from PIL import Image
from os import listdir
import os
from os.path import isfile, join
import string
import random
import shutil

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def process_files(folder):
    mypath = "/tmp/"+folder
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles = sorted(onlyfiles)
    final = []
    for i in onlyfiles:
        #print(i)
        im = Image.open(mypath+i)
        final.append(im)
    final[0].save(mypath+"SR.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=final[1:])


@app.route('/twopage',methods=['POST'])
def twopage():
    try:
        folder = id_generator() + "/"
        if not os.path.exists("/tmp/"+folder):
            os.makedirs("/tmp/"+folder)
        if request.method == 'POST':
            for i in request.files.getlist('file'):
                i.save(os.path.join("/tmp/"+folder,secure_filename(i.filename)))
            process_files(folder)
        return send_file("/tmp/"+folder+"SR.pdf", attachment_filename='SR.pdf')
    finally:
        shutil.rmtree("/tmp/"+folder)

if __name__ == '__main__':
    app.run()