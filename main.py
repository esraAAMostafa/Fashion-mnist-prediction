# This is a sample Python script.

import os

import numpy
from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

from predection import run_example

UPLOAD_FOLDER = '/Users/esraa/Documents/pythonProject/Fash'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class Classify(Resource):
    def get(self):
        result = int(run_example('sample.png'))
        my_array = numpy.array(['T- shirt / top', 'Trouser', 'Pullover', 'Dress',
                                'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'])
        return {'type': my_array[result]}, 200  # return data and 200 OK code

    pass


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadImage(Resource):
    def post(self):
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.rename(r'' + os.path.join(app.config['UPLOAD_FOLDER'], filename),
                      r'' + os.path.join(app.config['UPLOAD_FOLDER'], 'sample.png'))
            return 'success', 200

    pass


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)
api.add_resource(Classify, '/fashionPredection')
api.add_resource(UploadImage, '/uploadImage')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
