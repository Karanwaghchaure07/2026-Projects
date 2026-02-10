"""
Train face recognition model on collected dataset.
Saves trained model to MODELS_DIR.
"""
from src.config import RAW_FACES_DIR, MODELS_DIR
import os


def train_model():
    """
    Train recognizer on all face images in RAW_FACES_DIR.
    """
    print("Training model on collected faces...")
    # Training implementation
    pass


if __name__ == '__main__':
    train_model()
