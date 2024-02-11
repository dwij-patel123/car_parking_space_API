from flask import Flask,request
import os
from IPython.display import display,Image
from IPython import display
from ultralytics import YOLO

model = YOLO("yolov8m.pt") 
model.train(data="coco128.yaml", epochs=5)


