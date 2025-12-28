from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
import io
from PIL import Image

# Initialize the app
app = FastAPI(title="Visual Inspection API")

# Load the model once when the server starts
# Ensure 'best.pt' is in the same directory
try:
    model = YOLO("best.pt")
except Exception as e:
    print(f"Error loading model: {e}")
    # Fallback to standard model if custom one is missing for testing
    model = YOLO("yolov8n.pt") 

@app.get("/")
def home():
    return {"status": "healthy", "message": "Vision API is running. Go to /docs to test."}

@app.post("/detect/")
async def detect_defects(file: UploadFile = File(...)):
    # 1. Validate file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload JPEG or PNG.")

    # 2. Read the image
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image data.")

    # 3. Run inference
    # conf=0.25 is a standard confidence threshold
    results = model(image, conf=0.25) 

    # 4. Process results
    detections = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            # box.xyxy is [x_min, y_min, x_max, y_max]
            coordinates = box.xyxy[0].tolist() 

            detections.append({
                "class_name": class_name,
                "confidence": round(confidence, 2),
                "bbox": coordinates
            })

    return {
        "filename": file.filename, 
        "total_detections": len(detections),
        "detections": detections
    }