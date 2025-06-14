import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or replace with video file path

# Create the background subtractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Create a resizable window
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.namedWindow('Foreground Mask', cv2.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the background subtractor to get the foreground mask
    fgmask = fgbg.apply(frame)

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around detected motion
    for contour in contours:
        if cv2.contourArea(contour) < 500:  # Ignore small contours
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('Foreground Mask', fgmask)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
