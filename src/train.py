import os
import yaml
from ultralytics import YOLO
import torch

# -------------------------------------------------------------
# 1️⃣ Load Configuration
# -------------------------------------------------------------
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

project_name = config["project_name"]
model_type = config["model_type"]
num_classes = config["num_classes"]
paths = config["paths"]
train_cfg = config["training"]
log_cfg = config["logging"]

# -------------------------------------------------------------
# 2️⃣ Check Device
# -------------------------------------------------------------
device = "cuda" if torch.cuda.is_available() and train_cfg["device"] == "cuda" else "cpu"
print(f"✅ Using device: {device}")

# -------------------------------------------------------------
# 3️⃣ Create Dataset YAML for YOLO
# -------------------------------------------------------------
dataset_yaml = f"{project_name}_dataset.yaml"
dataset_yaml_path = os.path.join(os.getcwd(), dataset_yaml)

dataset_config = {
    "path": os.getcwd(),
    "train": paths["train_images"],
    "val": paths["val_images"],
    "names": ["oil_spill", "garbage_dump", "smoke_emission"]
}

with open(dataset_yaml_path, "w") as f:
    yaml.dump(dataset_config, f)

print(f"✅ Dataset YAML created at: {dataset_yaml_path}")

# -------------------------------------------------------------
# 4️⃣ Initialize YOLO Model
# -------------------------------------------------------------
model = YOLO("yolov8n.pt")  # You can change to yolov8s.pt or yolov8m.pt for better accuracy
model.info()

# -------------------------------------------------------------
# 5️⃣ Train the Model
# -------------------------------------------------------------
print("\n🚀 Starting Training...\n")
results = model.train(
    data=dataset_yaml_path,
    epochs=train_cfg["epochs"],
    imgsz=train_cfg["img_size"],
    batch=train_cfg["batch_size"],
    lr0=train_cfg["lr"],
    device=device,
    project=os.path.join(os.getcwd(), paths["results_dir"]),
    name="train_run",
    exist_ok=True
)

# -------------------------------------------------------------
# 6️⃣ Save Final Weights
# -------------------------------------------------------------
best_weights_path = os.path.join(paths["results_dir"], "train_run", "weights", "best.pt")

if log_cfg["save_checkpoint"]:
    if os.path.exists(best_weights_path):
        print(f"\n✅ Training complete. Best model saved at: {best_weights_path}")
    else:
        print("\n⚠️ Warning: Could not find best weights file!")
else:
    print("\nℹ️ Checkpoint saving disabled in config.yaml")

# -------------------------------------------------------------
# 7️⃣ Optional TensorBoard / Visualization
# -------------------------------------------------------------
if log_cfg["tensorboard"]:
    print("\n📊 You can start TensorBoard with:")
    print(f"tensorboard --logdir {os.path.join(paths['results_dir'], 'train_run')}")

print("\n🎯 Training completed successfully!")
