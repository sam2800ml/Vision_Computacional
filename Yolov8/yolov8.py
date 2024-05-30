import cv2
import numpy as np

# Load the ONNX model
net = cv2.dnn.readNetFromONNX("best (1).onnx")

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the frame for object detection
    input_image = cv2.resize(frame, (640, 640))  # Resize to the size your model expects
    blob = cv2.dnn.blobFromImage(input_image, scalefactor=1/255.0, size=(640, 640), swapRB=True, crop=False)
    net.setInput(blob)

    # Run the model
    detections = net.forward()

    # Process the detections
    for detection in detections[0]:
        confidence = detection[4]  # Assuming confidence is at index 4
        if confidence > 0.5:  # Confidence threshold
            class_id = int(detection[5])
            x_center = int(detection[0] * frame.shape[1])
            y_center = int(detection[1] * frame.shape[0])
            width = int(detection[2] * frame.shape[1])
            height = int(detection[3] * frame.shape[0])
            x_left = x_center - width // 2
            y_top = y_center - height // 2

            # Draw a bounding box
            cv2.rectangle(frame, (x_left, y_top), (x_left + width, y_top + height), (0, 255, 0), 2)
            label = f"Class {class_id}: {confidence:.2f}"
            cv2.putText(frame, label, (x_left, y_top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with detections
    cv2.imshow("Object Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
