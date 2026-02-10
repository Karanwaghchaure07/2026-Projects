"""
Attendance logging to CSV with duplicate prevention.
Handles writing attendance records and preventing duplicates.
"""
import csv
import os
from datetime import datetime
from src.config import ATTENDANCE_FILE, ATTENDANCE_DIR, DUPLICATE_PREVENTION_MINUTES


class AttendanceLogger:
    def __init__(self):
        """Initialize attendance logger."""
        os.makedirs(ATTENDANCE_DIR, exist_ok=True)
        self._init_csv()
    
    def _init_csv(self):
        """Initialize CSV file with headers if not exists."""
        if not os.path.exists(ATTENDANCE_FILE):
            with open(ATTENDANCE_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Date', 'Time', 'Status'])
    
    def mark_attendance(self, person_name):
        """
        Mark attendance for a person with duplicate prevention.
        
        Args:
            person_name: Name of the person
        """
        pass
    
    def is_duplicate(self, person_name):
        """
        Check if attendance was already marked recently.
        
        Args:
            person_name: Name of the person
            
        Returns:
            True if duplicate, False otherwise
        """
        pass
