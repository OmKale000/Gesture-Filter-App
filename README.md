# ✋ Gesture Filter App (Python)

Real-time **gesture-controlled video filter application** built with **Python, OpenCV, and MediaPipe**.  
Apply dynamic filters on video streams using intuitive **hand gestures** or via **Streamlit UI**.

---

### 🚀 Features

- ✅ Tracks both hands to detect **index finger** and **thumb** positions  
- 🎨 Polygon-shaped **ROI filter application** based on fingertip positions  
- 🔘 Round, user-friendly **UI buttons** on left and right screen edges  
- 🎭 Two sets of filters controllable via **gestures or UI**  
- 🔄 Reset buttons to revert to original unfiltered video  
- 📏 Adjustable window size with smooth real-time performance  

---

### ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/gesture-filter-app-python.git
   cd gesture-filter-app-python

---

### Set up a virtual environment (recommended)
```bash
python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate
```
---

### Install dependencies
```
pip install -r requirements.txt
```
---

### ▶️ Usage
Desktop App (OpenCV window)
```
python -m gesture_filter_app.main
```
---

### 🎮 Controls & Interaction

- 📷 Show your webcam video stream
- ✋ Use hand gestures to control filter selection
- 🖱️ Or use sidebar UI controls (Streamlit mode)
- ➕ Apply multiple overlapping filters
- 🔄 Use "Orig" buttons to reset filters
- 🔺 ROI polygon formed by index & thumb fingertips

---

### 📂 Project Structure
```
gesture-filter-app-python/
├── requirements.txt      # Python dependencies
├── gesture_filter_app/
│   ├── filters/          # Filter implementations
│   ├── hand_tracking/    # MediaPipe-based hand tracking
│   ├── ui/               # UI drawing utilities
│   ├── config.py         # Configuration constants
│   ├── main.py           # Desktop app entry point
│   ├── __main__.py       # Enables `python -m gesture_filter_app`
│   └── ...
├── README.md             # This file
└── LICENSE
```
---

### 📦 Dependencies
```
Python 3.8 – 3.11
OpenCV
MediaPipe
NumPy
```

Install them all:
```
pip install -r requirements.txt
```
---

### 🤝 Contributions

Contributions, issues, and feature requests are welcome!
Check the issues page

---

### 👤 Contact

Created by Om Kale

Email : ok176471@gmail.com

Special Credit: project idea inspired by @avani.artxtech

💌 Reach out for questions or collaborations!
