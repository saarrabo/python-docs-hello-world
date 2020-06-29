#from pyimagesearch.transform import four_point_transform
#from skimage.filters import threshold_local
import numpy as np
import cv2
#import imutils
from flask import Flask, request, Response, send_file
import jsonpickle
app = Flask(__name__)

@app.route('/api/detectcard', methods=['POST'])
def detectcard():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return r.data
