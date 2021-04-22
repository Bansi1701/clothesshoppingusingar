import cv2
import numpy as np
from flask import *

from base import app
from base.com.controller.camera import *
from base.com.dao.product_dao import ProductDAO


@app.route('/user/load', methods=['GET'])
def load_detection():
    try:
        product_id = request.args.get('product_id')
        product_dao = ProductDAO()
        product_vo_list = product_dao.selected_view_product(product_id)
        print("product vo list>>>>>", product_vo_list)

        session['product_image_path'] = (request.args.get('product_image_path')).replace("..", "base")
        session['product_image_name'] = request.args.get('product_image_name')
        return render_template("user/product-extended.html", product_vo_list=product_vo_list)
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


@app.route('/user/load_detection', methods=['GET'])
def user_load_detection():
    try:
        product_id = request.args.get('product_id')
        product_image_name = session.get('product_image_name')
        product_image_path = session.get('product_image_path')
        print('product_image_path>>>', product_image_path + product_image_name)
        return Response(gen(VideoCamera(), image=product_image_path + product_image_name),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as ex:
        print("admin_load_login route exception occured>>>>>>>>>>", ex)


def transparentOverlay(src, overlay, w, pos=(0, 0), scale=5):
    if w < 60:
        overlay = cv2.resize(overlay, (50, 50), fx=scale, fy=scale)
    if w > 60 and w < 100:
        overlay = cv2.resize(overlay, (350, 350), fx=scale, fy=scale)
    elif w > 100 and w < 150:
        overlay = cv2.resize(overlay, (450, 450), fx=scale, fy=scale)
    else:
        overlay = cv2.resize(overlay, (500, 500), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of pngImg
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of PngImage

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel

            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]

    return src


def gen(camera, image):
    face_cascade = cv2.CascadeClassifier('base/static/adminResources/models/haarcascade_frontalface_default.xml')
    # image='t5.png'
    pngImage = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    pngImage = cv2.resize(pngImage, (150, 150))
    # myvar =  request.form.get("Button1")
    # print('>>>>>>>>>>>>>>>>>>>>>>>>',myvar)
    print("every time")
    while True:
        frame = camera.get_frame()
        nparr = np.fromstring(frame, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
        print(frame.shape)
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            if w < 60:
                result = transparentOverlay(frame, pngImage, w, ((x + w // 2) - 150, (y + h // 2) + 50), 0.7)
            if w > 60 and w < 100:
                result = transparentOverlay(frame, pngImage, w, ((x + w // 2) - 160, (y + h // 2) + 40), 0.7)
            elif w > 100 and w < 150:
                result = transparentOverlay(frame, pngImage, w, ((x + w // 2) - 210, (y + h // 2) + 50), 0.7)
            else:
                result = transparentOverlay(frame, pngImage, w, ((x + w // 2) - 230, (y + h // 2) + 60), 0.7)
            result = cv2.imencode('.jpeg', result)[1].tostring()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + result + b'\r\n\r\n')
