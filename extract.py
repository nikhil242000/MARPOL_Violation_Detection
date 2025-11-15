

import cv2
import os

# --- Configuration ---
video_path = r"C:\Users\hp\Downloads\videoplayback (2).mp4"  # Path to your video file
output_folder = "frames_420x420" # Folder to save frames
frame_size = (420, 420)          # Desired frame size (width, height)
frame_interval = 1               # Extract every 1 frame (you can change this)

# --- Create output folder if not exists ---
os.makedirs(output_folder, exist_ok=True)

# --- Load video ---
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Stop when no frame is left

    # Extract frame at intervals (optional)
    if frame_count % frame_interval == 0:
        resized_frame = cv2.resize(frame, frame_size)
        frame_name = "shi1p_{:04d}.jpg".format(saved_count)
        cv2.imwrite(os.path.join(output_folder, frame_name), resized_frame)
        saved_count += 1

    frame_count += 1

cap.release()
print("✅ Extraction complete! {} frames saved in '{}'.".format(saved_count, output_folder))
