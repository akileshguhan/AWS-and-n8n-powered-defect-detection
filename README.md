# 🏗️ Automated Visual Inspection System (AWS & AI-Powered)

This project is an end-to-end **AI-powered defect detection pipeline**. It automatically analyzes images uploaded to the cloud to detect structural defects (like cracks in walls) and triggers automated workflows for reporting.

It combines **Deep Learning (YOLOv8)** for vision, **FastAPI** for the backend, **AWS** for cloud infrastructure, and **n8n** for workflow automation.

---

## 🚀 Key Features
- **AI-Powered Detection:** Uses a custom-trained YOLOv8 model to detect cracks and structural defects with high confidence.
- **Cloud Storage Integration:** Automatically processes images as soon as they are uploaded to an **AWS S3 Bucket**.
- **Scalable Backend:** Hosted on **AWS EC2**, serving predictions via a high-performance **FastAPI** interface.
- **Workflow Automation:** Integrates **n8n** to orchestrate the pipeline (S3 Trigger → AI Analysis → Alerting).
- **Real-time Tunneling:** Uses **ngrok** to expose local automation workflows to cloud events securely.

---

## 🛠️ Tech Stack

| Component | Technology Used |
| :--- | :--- |
| **AI Model** | YOLOv8 (Ultralytics), PyTorch |
| **Backend API** | FastAPI, Uvicorn, Python 3.9+ |
| **Cloud Infrastructure** | AWS EC2 (t2.micro), AWS S3 |
| **Automation** | n8n (Dockerized) |
| **Tunneling** | ngrok |
| **Containerization** | Docker |

---

## 🏗️ Architecture

1.  **Input:** User/Drone uploads an image to **AWS S3**.
2.  **Trigger:** n8n watches the S3 bucket for new files.
3.  **Processing:**
    * n8n downloads the image.
    * n8n sends the image to the **FastAPI Server** (running on EC2).
    * **YOLOv8 Model** analyzes the image for defects.
4.  **Output:** The system returns JSON data containing bounding boxes and confidence scores.
5.  **Action (Planned):**
    * Log results to **PostgreSQL/AWS RDS**.
    * Create a **Jira Ticket** if a defect is severe.
    * Send a **Slack Alert** to the engineering team.

---

## ⚙️ Setup & Installation

### 1. AI Backend (FastAPI)
```bash
# Clone the repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server locally
uvicorn main:app --reload