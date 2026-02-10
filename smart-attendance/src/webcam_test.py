import cv2

def main():
    cap = cv2.VideoCapture(0)  # 0 = default camera

    if not cap.isOpened():
        print("❌ Could not open webcam. Try changing camera index to 1.")
        return

    print("✅ Webcam opened. Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        cv2.imshow("Webcam Test", frame)

        if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
