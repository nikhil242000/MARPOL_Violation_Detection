import streamlit as st
import cv2
import pandas as pd
import os
from datetime import datetime

# ===========================
# PAGE CONFIGURATION
# ===========================
st.set_page_config(page_title="MARPOL Violation Detection", layout="wide")
st.title("🌊 MARPOL Violation Detection Dashboard")
st.markdown("### Real-time Environmental Compliance Monitoring")
st.markdown("---")

# ===========================
# FILE PATHS
# ===========================
VIDEO_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\results\detected_output.mp4"
LOG_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\results\violation_log.csv"
METRICS_PATH = r"C:\Users\hp\Downloads\MARPOL_Violation_Detection\results\metrics_report.txt"

# ===========================
# SIDEBAR - METRICS
# ===========================
st.sidebar.header("📊 Model Performance Metrics")
if os.path.exists(METRICS_PATH):
    with open(METRICS_PATH, "r") as f:
        st.sidebar.text(f.read())
else:
    st.sidebar.info("Train the model to generate metrics.")

# ===========================
# VIDEO PLAYER (REAL-TIME)
# ===========================
st.header("🎥 Processed Detection Video Stream")

video_placeholder = st.empty()  # container for live video frames

if os.path.exists(VIDEO_PATH):
    cap = cv2.VideoCapture(VIDEO_PATH)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert color (BGR → RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize for dashboard
        frame = cv2.resize(frame, (720, 420))

        # Display video in Streamlit
        video_placeholder.image(frame, channels="RGB", use_container_width=True)

        current_frame += 1

        # Stop after full video
        if current_frame >= frame_count:
            break

    cap.release()
else:
    st.warning("No processed video found. Run `detect.py` first to generate it.")

st.markdown("---")

# ===========================
# LIVE VIOLATION LOG TABLE
# ===========================
st.header("📄 Recent MARPOL Violations")

if os.path.exists(LOG_PATH):
    df = pd.read_csv(LOG_PATH)
    df = df.sort_values(by="Timestamp", ascending=False)
    st.dataframe(df.head(10), use_container_width=True)
else:
    st.info("No violation logs found yet. Run detection to generate entries.")

# ===========================
# FOOTER
# ===========================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 14px;'>"
    "Developed by <b>Nikhil Dongare</b> | Powered by <b>YOLOv8 + Streamlit</b> | "
    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    "</div>",
    unsafe_allow_html=True
)
