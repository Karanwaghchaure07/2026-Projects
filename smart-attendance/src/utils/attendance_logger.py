import csv
import os
from datetime import datetime

ATTENDANCE_FILE = os.path.join("data", "attendance", "attendance.csv")
os.makedirs(os.path.dirname(ATTENDANCE_FILE), exist_ok=True)

HEADER = ["PersonID", "Name", "Date", "Time"]

def _ensure_header():
    """Create file + header if missing or empty."""
    if not os.path.exists(ATTENDANCE_FILE) or os.path.getsize(ATTENDANCE_FILE) == 0:
        with open(ATTENDANCE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)

def mark_attendance(person_id: str, name: str) -> bool:
    """
    Returns True if newly marked, False if already marked today.
    Prevent duplicates by (PersonID + Date).
    """
    _ensure_header()

    today = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M:%S")

    # Read existing rows safely
    already_marked = False
    rows = []

    with open(ATTENDANCE_FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            rows.append(row)

    # Detect header (first row non-numeric in col 0)
    start_idx = 1 if rows and (not rows[0][0].strip().isdigit()) else 0

    for row in rows[start_idx:]:
        # Expect: PersonID, Name, Date, Time
        if len(row) < 4:
            continue
        rid = row[0].strip()
        rdate = row[2].strip()
        if rid == person_id.strip() and rdate == today:
            already_marked = True
            break

    if already_marked:
        return False

    # Append new record
    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([person_id.strip(), name.strip(), today, now_time])

    return True
