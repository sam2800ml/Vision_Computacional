from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2.aruco as aruco


model = YOLO("Yolov8/best.pt")

cap = cv2.VideoCapture(0)

def aruco_caption(frame):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    parameters =  aruco.DetectorParameters_create()
    corners, _, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    pixel_cm_ratio = None
    if len(corners) > 0:
        for marker_corners in corners:
            marker_corners = marker_corners[0].astype(np.float32) 
            aruco_perimeter = cv2.arcLength(marker_corners,True)
            side_length_cm = 10
            perimeter_cm = 4 * side_length_cm  
            pixel_cm_ratio = aruco_perimeter / perimeter_cm
            rect = cv2.minAreaRect(marker_corners)
            (x, y), (w, h), angle = rect
          
            object_width = w / pixel_cm_ratio
            object_height = h / pixel_cm_ratio
    
            cv2.putText(frame, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(frame, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

    frame_markers = aruco.drawDetectedMarkers(frame, corners)
    return frame_markers, pixel_cm_ratio

def detection_model(frame,results,pixel_cm_ratio ,threshold=0.7):
    for i, result in enumerate(results.boxes.data.tolist()):
        x1, y1, x2, y2, score, class_id = result
        print(score)
        if score > threshold:
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
            print(f"Coordenadas:{ x1,y1,x2,y2}")
            print(f"Confianza {score}")
            print(f" Id: {class_id}")
            if pixel_cm_ratio:

                w = x2-x1
                h = y2-y1
                object_width = w / pixel_cm_ratio
                object_height = h / pixel_cm_ratio
                cv2.putText(frame, "Width {} cm".format(round(object_width, 1)), (int(x1 - 100), int(y1 - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                cv2.putText(frame, "Height {} cm".format(round(object_height, 1)), (int(x1 - 100), int(y1 + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

            cv2.rectangle(frame,(x1,y1),(x2,y2), (0,0,0),1)
            cv2.putText(frame, str(class_id), (x1,y1 -10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), cv2.LINE_AA)
            


            return frame
        return frame
    return frame
    


while True:
    ret, frame = cap.read()
    results = model.predict(frame)[0]
    frame, pixel_cm_ratio = aruco_caption(frame)
    frame = detection_model(frame,results, pixel_cm_ratio)
    cv2.imshow('frame', frame)
    
    # Espera a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()