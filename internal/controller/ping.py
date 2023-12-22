from flask import Flask, request, jsonify
import flask_expects_json as validator
from internal.model.model import ImageRequestBody
from keras.utils import get_file
from keras.utils import load_img


from keras.preprocessing import image as img
import numpy as np


import pkg.response.base as response


from keras.models import load_model
model = load_model("./model.h5")
modelvgg = load_model("./model_vgg.h5")
label_classes = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

def ping():
    return response.success_response("pong")

@validator.expects_json(ImageRequestBody)
def predict():
    req = request.json
    image_url = req['image_url']
    image_file = get_file(origin=image_url)
    image = load_img(image_file, target_size=(256,256))

    x = img.img_to_array(image)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=32)
    classesVGG = modelvgg.predict(images, batch_size=32)
    res = label_classes[np.argmax(classes)]
    resVGG = label_classes[np.argmax(classesVGG)]



    return response.success_response({"resnet":res,"vgg":resVGG})

    




def init_routes(app: Flask):
    app.route("/ping",methods=['GET'])(ping)
    app.route("/classify",methods=['POST'])(predict)
    