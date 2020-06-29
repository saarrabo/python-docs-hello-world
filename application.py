from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils
from flask import Flask, request, Response, send_file
import jsonpickle
app = Flask(__name__)

@app.route('/api/detectcard', methods=['POST'])
def detectcard():
    r = request
    # convert string of image data to uint8
    print(r.data)
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #cv2.imshow("Server", image)
    #cv2.waitKey(0)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height = 500)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0, 0)
    edged = cv2.Canny(gray, 80, 200)


    print("STEP 1: Edge Detection")
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]


    for c in cnts:
	# approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        print(len(approx))
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break

    print("STEP 2: Find contours of paper")
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)

    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)


    print("STEP 3: Apply perspective transform")
    cv2.imwrite("Server_image.jpg", imutils.resize(warped, height = 650))
    filename = "Server_image.jpg"
    _, img_encoded = cv2.imencode('.jpg', warped)
    data=img_encoded.tostring()
    response = {'message': data}
    return send_file(filename, mimetype='image/jpg', attachment_filename='processed.jpg')
