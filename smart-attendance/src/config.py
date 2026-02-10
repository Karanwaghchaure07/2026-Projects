"""Configuration settings for Smart Attendance System"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_FACES_DIR = os.path.join(DATA_DIR, 'raw_faces')
MODELS_DIR = os.path.join(DATA_DIR, 'models')
ATTENDANCE_DIR = os.path.join(DATA_DIR, 'attendance')
SAMPLES_DIR = os.path.join(DATA_DIR, 'samples')

# Camera settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Face detection thresholds
CONFIDENCE_THRESHOLD = 0.5
MIN_NEIGHBORS = 5

# Attendance settings
ATTENDANCE_FILE = os.path.join(ATTENDANCE_DIR, 'attendance.csv')
DUPLICATE_PREVENTION_MINUTES = 5
