# 💊 MedScan AI

MedScan AI is a smart healthcare assistant that scans medicine strips to provide **expiry dates, usage instructions, benefits, and disadvantages** instantly.  
This project aims to make medicine information easily accessible and user-friendly.

---

## 🚀 Features
- 📷 Upload and scan medicine strips  
- 📅 Detect expiry date of medicines  
- 📖 Show usage instructions clearly  
- ✅ List benefits and possible side effects  
- 🌐 Simple and clean user interface  

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript (React for UI)  
- **Backend:** Python (Flask)  
- **Database:** SQLite / CSV (for medicine data)  
- **ML/AI:** OCR for text extraction  
- **Deployment:** Render / GitHub Pages  

---

## ⚙️ Installation & Setup

Clone the repository:
```bash
git clone https://github.com/gshalini8/Medscan-ai.git
cd Medscan-ai
```

Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the app locally:
```bash
python app.py
```

Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🌍 Deployment
This project can be deployed using **Render** or any cloud platform that supports Python & Flask.  
Update `render.yaml` for automatic deployment.

---

## 📂 Project Structure
```
Medscan-AI/
│── app.py               # Flask main app
│── render.yaml          # Render deployment config
│── requirements.txt     # Dependencies
│── static/              # CSS, JS, Images
│── templates/           # HTML templates
│── uploads/             # Uploaded medicine images
│── notebooks/           # Jupyter notebooks for analysis
│── data/                # Medicine dataset
│── README.md            # Project documentation
```

---

## 👩‍💻 Author
**Shalini G**  
B.Tech, Data Science Enthusiast  

---

## 📜 License
This project is licensed under the MIT License.

---

✨ *MedScan AI – Making healthcare information simple & accessible!* ✨
