from ultralytics import YOLO

model = YOLO("models/best_model.pt")

metrics = model.val(data="data/dataset.yaml")
with open("results/metrics_report.txt", "w") as f:
    f.write(str(metrics))

print("✅ Validation complete. Metrics saved to results/metrics_report.txt")
