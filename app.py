from flask import Flask, render_template, request, jsonify
import os
import pytesseract
from PIL import Image
import pandas as pd
from fuzzywuzzy import process
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load medicine data
df = pd.read_csv('data/medicine_info.csv')
medicine_data = df.set_index('name').T.to_dict()
medicine_names = list(medicine_data.keys())

# 🔍 Debug-friendly medicine matching
def find_medicine_info(text):
    print("OCR text for matching:", text)
    words = re.sub(r'[^a-zA-Z\s]', '', text).lower().split()
    print("Words from OCR:", words)
    for word in words:
        match, score = process.extractOne(word, medicine_names)
        print(f"Trying word: {word} → Best match: {match} (Score: {score})")
        if score >= 80:
            return match, medicine_data[match]
    return None, None

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Scan route
@app.route('/scan', methods=['POST'])
def scan():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    # OCR text extraction
    text = pytesseract.image_to_string(Image.open(path)).lower().strip().replace("\n", " ")
    print("🧾 OCR Result:", text)

    # Find medicine info
    medicine, info = find_medicine_info(text)
    if not medicine:
        return jsonify({'error': 'Medicine not recognized'}), 404

    return jsonify({'medicine': medicine, 'info': info})

# ✅ Run the app on port 5001
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
