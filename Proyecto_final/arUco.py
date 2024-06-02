import cv2
import cv2.aruco as aruco
import numpy as np

def aruco_caption(frame):
    # Obtiene el diccionario de marcadores ArUco
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    # Configura los parámetros del detector
    parameters =  aruco.DetectorParameters_create()
    # Detecta los marcadores ArUco en la imagen
    corners, _, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    print(corners)
    
    return corners



cap = cv2.VideoCapture(0)

while True:
    # Captura el frame de la cámara
    ret, frame = cap.read()
    
    # Convierte el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners = aruco_caption(gray)
    
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
        
        # Dibuja los marcadores detectados en el frame
        frame = aruco.drawDetectedMarkers(frame, corners)
    
    
    # Dibuja los marcadores detectados en el frame
    frame_markers = aruco.drawDetectedMarkers(frame, corners)
    
    # Muestra el frame con los marcadores
    cv2.imshow('frame', frame)
    
    # Espera a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()
