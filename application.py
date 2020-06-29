#from pyimagesearch.transform import four_point_transform
#from skimage.filters import threshold_local
#import numpy as np
#import argparse
#import cv2
#import imutils
from flask import Flask, request, Response, send_file
import jsonpickle
app = Flask(__name__)

@app.route('/api/detectcard', methods=['POST'])
def detectcard():
    response = {'message': data}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype='application/json')
