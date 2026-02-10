import cv2
import csv
import os
from utils.face_detector import detect_faces
from utils.attendance_logger import mark_attendance

MODEL_PATH = os.path.join("data", "models", "lbph_model.xml")
PEOPLE_CSV = os.path.join("data", "raw_faces", "people.csv")

# Load ID → Name mapping
id_to_name = {}
with open(PEOPLE_CSV, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        id_to_name[int(row["person_id"])] = row["name"]

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_PATH)

cap = cv2.VideoCapture(0)

print("🎥 Camera started. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        if confidence < 80:  # lower = better
            name = id_to_name.get(label, "Unknown")
            marked = mark_attendance(str(label).zfill(3), name)
            text = f"{name} ({confidence:.1f})"
        else:
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
        break

cap.release()
cv2.destroyAllWindows()
