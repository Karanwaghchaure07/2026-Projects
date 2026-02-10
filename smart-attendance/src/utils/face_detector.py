import cv2

# Load Haar Cascade
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def detect_faces(gray_frame):
    """
    Detect faces in a grayscale frame.
    Returns list of (x, y, w, h)
    """
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.3,
        minNeighbors=5
    )
    return faces
