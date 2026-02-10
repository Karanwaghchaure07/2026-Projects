# Quick Demo Guide (1 Minute)

## Step 1: Setup

```bash
pip install -r requirements.txt
```

## Step 2: Capture Faces

```bash
python -m src.capture_faces
```

- Enter name when prompted
- Let the script capture 30 images per person

## Step 3: Train Model

```bash
python -m src.train_model
```

- Model will be trained on captured images
- Saved to `data/models/`

## Step 4: Run Attendance

```bash
python -m src.recognize_attendance
```

- Point camera at faces
- Attendance automatically logged to `data/attendance/attendance.csv`
- Press 'q' to quit

## Output

Check `data/attendance/attendance.csv` for attendance records.
