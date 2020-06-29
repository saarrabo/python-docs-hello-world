#from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils
from flask import Flask, request, Response, send_file
import jsonpickle
app = Flask(__name__)

@app.route('/api/detectcard', methods=['POST'])
def detectcard():
    # r = request
    # convert string of image data to uint8
    # nparr = np.fromstring(r.data, np.uint8)
    # decode image
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")	
