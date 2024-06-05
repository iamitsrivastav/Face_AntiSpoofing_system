from ultralytics import YOLO

model = YOLO('yolov8n.pt')


model.train(data='Dataset/SplitData/dataoffline.yaml',epochs=10)


