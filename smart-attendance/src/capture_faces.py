import cv2
import os
from utils.face_detector import detect_faces

def capture_faces(person_id: str, person_name: str, num_images: int = 40):
    folder_name = f"{person_id}_{person_name}"
    save_dir = os.path.join("data", "raw_faces", folder_name)
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return

    count = 0
    print(f"✅ Capturing for {folder_name}")
    print("Tip: Look at camera, change angles slightly. Press Q to quit early.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(gray)

        # pick the largest face (best for single-person capture)
        if len(faces) > 0:
            x, y, w, h = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)[0]

            # draw rectangle for feedback
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

            # crop face (use grayscale for training consistency)
            face_crop = gray[y:y+h, x:x+w]
            face_crop = cv2.resize(face_crop, (200, 200))

            # save every few frames to avoid near-duplicates
            if count < num_images:
                filename = os.path.join(save_dir, f"img_{count+1:03d}.jpg")
                cv2.imwrite(filename, face_crop)
                count += 1

        cv2.putText(frame, f"Saved: {count}/{num_images}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Capture Faces", frame)

        if (cv2.waitKey(1) & 0xFF) in (ord("q"), ord("Q")):
            break

        if count >= num_images:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"✅ Done. Saved {count} images in {save_dir}")

if __name__ == "__main__":
    # Change these for each person
    capture_faces("002", "Person2", num_images=40)
