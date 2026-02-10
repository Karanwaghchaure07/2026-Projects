import csv
import os
from datetime import datetime

ATTENDANCE_FILE = os.path.join("data", "attendance", "attendance.csv")
os.makedirs(os.path.dirname(ATTENDANCE_FILE), exist_ok=True)

def mark_attendance(person_id, name):
    today = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M:%S")

    already_marked = False

    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == person_id and row[2] == today:
                    already_marked = True
                    break

    if not already_marked:
        with open(ATTENDANCE_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([person_id, name, today, now_time])
        return True

    return False
