import cv2
import os
import numpy as np

DATASET_DIR = os.path.join("data", "raw_faces")
MODEL_DIR = os.path.join("data", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "lbph_model.xml")

os.makedirs(MODEL_DIR, exist_ok=True)

def load_dataset():
    faces = []
    labels = []

    for folder in os.listdir(DATASET_DIR):
        if "_" not in folder:
            continue

        label = int(folder.split("_")[0])
        person_dir = os.path.join(DATASET_DIR, folder)

        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue

            faces.append(img)
            labels.append(label)

    return faces, np.array(labels)

if __name__ == "__main__":
    print("📂 Loading dataset...")
    faces, labels = load_dataset()

    print(f"✅ Loaded {len(faces)} face images")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, labels)

    recognizer.save(MODEL_PATH)
    print(f"🎉 Model trained and saved to {MODEL_PATH}")
