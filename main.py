from flask import Flask, request, make_response
from flask_restful import reqparse, Resource, Api
import numpy as np
import pdb

from encode import Encoder
from decode import Decoder

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('hexcode', type=str)

class Hex(Resource):
    def get(self):
        return "Coming soon"
    def post(self):
        if 'image' in request.files:
            image_arr = np.fromstring(request.files['image'].read(), np.uint8)
            decoder = Decoder(image_arr)
            return decoder.decode()
        return "Error finding file, please upload image with key 'image'"

class Encode(Resource):
    def get(self):
        args = parser.parse_args()
        if 'hexcode' in args:
            hexcode = str(args['hexcode'])
            encoder = Encoder(hexcode)

            response = make_response(encoder.encode())
            response.headers['Content-Type'] = 'image/png'

            return response
        return "No hexcode to encode provided."

api.add_resource(Hex, '/')
api.add_resource(Encode, '/encode')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
