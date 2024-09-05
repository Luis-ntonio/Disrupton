from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("runs/classify/train2/weights/best.pt")  # load a custom model


results = model.predict(source="0", show=True)
