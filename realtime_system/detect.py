# import cv2
# import os
# from ultralytics import YOLO
# import time

# # =========================
# # CONFIGURATION
# # =========================
# MODEL_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\src\results\train_run\weights\best.pt"
# VIDEO_PATH = r"C:\Users\hp\Downloads\Waste Dumping By Ships 🤯.mp4"  # or 0 for webcam
# OUTPUT_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\results\detected_output1.mp4"
# CONF_THRESHOLD = 0.3

# # =========================
# # LOAD MODEL
# # =========================
# print(f"Loading model from: {MODEL_PATH}")
# model = YOLO(MODEL_PATH)

# # =========================
# # LOAD VIDEO
# # =========================
# cap = cv2.VideoCapture(VIDEO_PATH)
# if not cap.isOpened():
#     print(f"Error: Could not open video: {VIDEO_PATH}")
#     exit()

# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)

# # Create output directory if not exists
# os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# # Video writer
# out = cv2.VideoWriter(
#     OUTPUT_PATH,
#     cv2.VideoWriter_fourcc(*"mp4v"),
#     fps,
#     (frame_width, frame_height)
# )

# # =========================
# # RUN DETECTION
# # =========================
# print("Starting detection... Press 'q' to quit.")
# start_time = time.time()
# frame_count = 0

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Perform detection
#     results = model(frame, conf=CONF_THRESHOLD)

#     # Visualize detections on frame
#     annotated_frame = results[0].plot()

#     # Display results
#     cv2.imshow("MARPOL Violation Detection", annotated_frame)
#     out.write(annotated_frame)
#     frame_count += 1

#     # Press 'q' to stop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

# end_time = time.time()
# print(f"✅ Detection completed. Processed {frame_count} frames in {end_time - start_time:.2f} seconds.")
# print(f"🎥 Output saved to: {OUTPUT_PATH}")


# import cv2
# import os
# from ultralytics import YOLO
# import time

# # =========================
# # CONFIGURATION
# # =========================
# MODEL_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\src\results\train_run\weights\best.pt"
# VIDEO_PATH = r"C:\Users\hp\Downloads\videoplayback (3).mp4"  # or 0 for webcam
# OUTPUT_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\results\detected_output3.mp4"
# CONF_THRESHOLD = 0.3

# # =========================
# # LOAD MODEL
# # =========================
# print(f"Loading model from: {MODEL_PATH}")
# model = YOLO(MODEL_PATH)

# # =========================
# # LOAD VIDEO
# # =========================
# cap = cv2.VideoCapture(VIDEO_PATH)
# if not cap.isOpened():
#     print(f"Error: Could not open video: {VIDEO_PATH}")
#     exit()

# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)

# # Create output directory if not exists
# os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# # Video writer
# out = cv2.VideoWriter(
#     OUTPUT_PATH,
#     cv2.VideoWriter_fourcc(*"mp4v"),
#     fps,
#     (frame_width, frame_height)
# )

# # =========================
# # RUN DETECTION
# # =========================
# print("Starting detection... Press 'q' to quit.")
# start_time = time.time()
# frame_count = 0

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Perform detection
#     results = model(frame, conf=CONF_THRESHOLD)

#     # Visualize detections on frame
#     annotated_frame = results[0].plot()

#     # Resize window to 420x620 for display
#     display_frame = cv2.resize(annotated_frame, (620, 420))

#     # Display results
#     cv2.imshow("MARPOL Violation Detection", display_frame)
#     out.write(annotated_frame)
#     frame_count += 1

#     # Press 'q' to stop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

# end_time = time.time()
# print(f"✅ Detection completed. Processed {frame_count} frames in {end_time - start_time:.2f} seconds.")
# print(f"🎥 Output saved to: {OUTPUT_PATH}")







import cv2
import os
import csv
import time
from ultralytics import YOLO

# =========================
# CONFIGURATION
# =========================
MODEL_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\src\results\train_run\weights\best.pt"
VIDEO_PATH = r"C:\Users\hp\Downloads\videoplayback (1).mp4"  # or 0 for webcam
OUTPUT_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\results\detected_output.mp4"
LOG_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\results\violation_log.csv"
CONF_THRESHOLD = 0.2

# =========================
# LOAD MODEL
# =========================
print(f"Loading model from: {MODEL_PATH}")
model = YOLO(MODEL_PATH)

# =========================
# PREPARE VIDEO
# =========================
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print(f"Error: Could not open video: {VIDEO_PATH}")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

out = cv2.VideoWriter(
    OUTPUT_PATH,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (frame_width, frame_height)
)

# =========================
# LOG FILE SETUP
# =========================
with open(LOG_PATH, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Timestamp", "Frame", "Class", "Confidence"])

# =========================
# RUN DETECTION
# =========================
print("Starting detection... Press 'q' to quit.")
frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=CONF_THRESHOLD)
    annotated_frame = results[0].plot()

    # Resize for display
    display_frame = cv2.resize(annotated_frame, (620, 420))
    cv2.imshow("MARPOL Violation Detection", display_frame)
    out.write(annotated_frame)

    # Log detections
    detections = results[0].boxes
    if detections is not None and len(detections) > 0:
        with open(LOG_PATH, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for det in detections:
                cls_id = int(det.cls)
                conf = float(det.conf)
                label = model.names[cls_id]
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([timestamp, frame_count, label, round(conf, 3)])

    frame_count += 1
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print(f"✅ Detection complete. Saved: {OUTPUT_PATH}")
print(f"📘 Log saved: {LOG_PATH}")
