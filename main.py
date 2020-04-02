from flask import Flask, request
from flask_restful import Resource, Api
import numpy as np
import pdb
from decode import Decoder

app = Flask(__name__)
api = Api(app)

class Hex(Resource):
    def get(self):
        return "Coming soon"
    def post(self):
        if 'image' in request.files:
            image_arr = np.fromstring(request.files['image'].read(), np.uint8)
            decoder = Decoder(image_arr)
            return decoder.decode()
        return "Error finding file, please upload image with key 'image'"

api.add_resource(Hex, '/')

if __name__ == '__main__':
    app.run(debug=True)
