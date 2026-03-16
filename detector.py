# detector.py
import cv2 as cv
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolov8x.pt"):
        self.model = YOLO(model_path)
        self.target_classes = [0, 2, 3, 5, 7]

    def detect_and_draw(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            classes=self.target_classes,
            conf=0.36,
            verbose=False,
            device=0
        )

        display_frame = frame.copy()
        person_count = 0
        vehicle_count = 0

        if results[0].boxes is not None and results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.int().cpu().tolist()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            clss = results[0].boxes.cls.int().cpu().tolist()
            confs = results[0].boxes.conf.cpu().tolist()

            for box, track_id, cls_id, conf in zip(boxes, track_ids, clss, confs):
                x1, y1, x2, y2 = box

                if cls_id == 0:
                    person_count += 1
                    label_name = "Person"
                    color = (0, 150, 255) # 주황색
                else:
                    vehicle_count += 1
                    color = (150, 255, 0) # 연두색
                    if cls_id == 2: label_name = "Car"
                    elif cls_id == 3: label_name = "Bike"
                    elif cls_id == 5: label_name = "Bus"
                    elif cls_id == 7: label_name = "Truck"

                text = f"{label_name} #{track_id} ({int(conf * 100)}%)"

                cv.rectangle(display_frame, (x1, y1), (x2, y2), color, 2)

                font = cv.FONT_HERSHEY_SIMPLEX
                font_scale = 0.5
                thickness = 1
                (text_w, text_h), _ = cv.getTextSize(text, font, font_scale, thickness)
                cv.rectangle(display_frame, (x1, y1 - text_h - 8), (x1 + text_w + 4, y1), color, -1)

                cv.putText(display_frame, text, (x1 + 2, y1 - 4), font, font_scale, (0, 0, 0), thickness)

        cv.putText(display_frame, f"Person: {person_count}", (20, 40),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 150, 255), 2)
        cv.putText(display_frame, f"Vehicle: {vehicle_count}", (20, 75),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (150, 255, 0), 2)

        return display_frame