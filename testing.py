from ultralytics import YOLO
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0)

# Load a model
model = YOLO("runs/classify/train2/weights/best.pt")  # load a custom model

# object classes
classNames = ["No Desechables", "No Desechables", "Papel y Carton", "Plastico", "Plastico", "Plastico", "Papel y Carton", "Papel y Carton", "Plastico", "Plastico", "Papel y Carton", "No Desechables", "Plastico", "No Desechables", "No Desechables", "Plastico", "Organicos", "Plastico", "Organicos", "No Desechables", "Papel y Carton", "No Desechables", "Organicos", "Plastico", "Plastico", "No Desechables"]


while True:
    success, img = cap.read()
    height, width, channels = img.shape
    results = model(img, stream=False, conf=0.8)

    # coordinates
    for r in results:
        if r.probs.top1conf >= 0.8:
            cv2.rectangle(img, (0, 0), (width, 50), (255, 255, 255), -1)
            text = f"Depositar objeto en el tacho {classNames[r.probs.top1]}"
            org = [0, 30]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 0.7
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, text, org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
