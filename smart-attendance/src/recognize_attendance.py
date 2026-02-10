"""
Real-time face recognition and attendance marking.
Recognizes faces from camera and logs attendance to CSV.
"""
from src.config import CAMERA_INDEX, MODELS_DIR
from src.utils.face_detector import FaceDetector
from src.utils.attendance_logger import AttendanceLogger


def run_recognition():
    """Start real-time face recognition and mark attendance."""
    detector = FaceDetector()
    logger = AttendanceLogger()
    
    print("Starting face recognition...")
    print("Press 'q' to quit")
    
    # Recognition loop implementation
    pass


if __name__ == '__main__':
    run_recognition()
