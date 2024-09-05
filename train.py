from ultralytics import YOLO
import torch


def main():
    print(torch.cuda.is_available())
    torch.cuda.set_device(0)
    # Load a model
    model = YOLO("yolov8x-cls.pt")  # load a pretrained model (recommended for training)
    
    # Train the model with 2 GPUs
    results = model.train(data="Data", epochs=50, weight_decay=0.001, dropout=0.1, optimizer="SGD", device="0", hsv_h = 0.03, hsv_s = 0.65, hsv_v = 0.5, degrees = 90.0, bgr = 0.2, erasing = 0.45, crop_fraction = 1.0)

if __name__ == "__main__":
    main()