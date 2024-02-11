from flask import Flask, request, jsonify, render_template
import os
from IPython.display import display,Image
from IPython import display
from ultralytics import YOLO
import numpy

model = YOLO("runs/detect/train2/weights/best.pt")
results = model.predict(source="Parking-space-Detection-1/test/images/2013-04-15_07_25_01_jpg.rf.6cfda5e6abb67e42f01965fafe80d37b.jpg",conf=0.2,show=True)




