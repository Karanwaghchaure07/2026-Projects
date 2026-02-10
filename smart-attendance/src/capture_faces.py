"""
Capture face images for dataset collection.
Stores images per person in RAW_FACES_DIR.
"""
from src.config import CAMERA_INDEX, RAW_FACES_DIR
from src.utils.face_detector import FaceDetector


def capture_faces(person_name, num_samples=30):
    """
    Capture face samples for a person.
    
    Args:
        person_name: Name of the person
        num_samples: Number of face samples to capture
    """
    detector = FaceDetector()
    detector.capture_faces(person_name, num_samples)


if __name__ == '__main__':
    person_name = input("Enter person name: ")
    num_samples = int(input("Number of samples (default 30): ") or "30")
    capture_faces(person_name, num_samples)
