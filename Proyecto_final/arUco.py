import cv2
import cv2.aruco as aruco


cap = cv2.VideoCapture(0)

while True:
    # Captura el frame de la cámara
    ret, frame = cap.read()
    
    # Convierte el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Obtiene el diccionario de marcadores ArUco
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    
    # Configura los parámetros del detector
    parameters =  aruco.DetectorParameters_create()
    
    # Detecta los marcadores ArUco en la imagen
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    # Dibuja los marcadores detectados en el frame
    frame_markers = aruco.drawDetectedMarkers(frame, corners)
    
    # Muestra el frame con los marcadores
    cv2.imshow('frame', frame_markers)
    
    # Espera a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()
