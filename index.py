from flask import Flask, request, jsonify, render_template
import os
from IPython.display import display,Image
from IPython import display
from ultralytics import YOLO
import numpy


app = Flask(__name__)
model = YOLO("runs/detect/train2/weights/best.pt")


@app.route("/")
def home():
    return "API is running"

@app.route("/car_lot",methods=["POST"])
def get_car_id():
    if(request.data):
        request_data = request.get_json()
        time = request_data["curr_time"]
        lot_num = request_data["number"]
        total_spaces = request_data["total_spaces"]
        results = model.predict(source="extracted_images/lot_{}/{}.png".format(lot_num,time*4),conf=0.5)

        boxes = results[0].boxes
        classes = boxes.cls


        classes = classes.numpy()

        count = 0
        for cl in classes:
            if(cl == 2):
                count+=1
        spaces_empty = total_spaces-count
        return [spaces_empty]
    else:
        return "No data given"
    

if __name__ == "__main__":
    app.debug = True
    app.run()  