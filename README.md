# 📊 ATS Resume Tracker

An AI-powered **Applicant Tracking System (ATS)** built with Python, Streamlit, and the modern Google Gen AI SDK. This application allows job seekers to evaluate their resumes against any job description across diverse industries using the cutting-edge **Gemini 3.8 Flash** model.

It provides detailed professional evaluations, highlights profile strengths and weaknesses, calculates automated ATS match percentages, and identifies missing keywords.

---

## 🌐 Live Application

🚀 **The project is officially hosted and live!** You can use the web interface directly without any local installation here:

👉 <a href="https://ats-tracker-g2.streamlit.app/" target="_blank" rel="noopener noreferrer">**Open Live App on Streamlit Cloud**</a>

---

## ✨ Features

- **Multimodal Evaluation:** Seamlessly handles resumes uploaded as PDF documents.
- **Deep HR Analysis:** Acts as an expert Talent Acquisition Specialist to provide an objective breakdown of a candidate's alignment, strengths, and weaknesses for a specific role.
- **ATS Match Score & Keyword Gap Detection:** Simulates real-world recruitment software to compute a realistic match percentage and extract crucial missing keywords.
- **Modern Gemini API Integration:** Built using the current standard `google-genai` SDK and the `gemini-3.8-flash` model.
- **Production-Ready Hosting Support:** Fully configured with `packages.txt` for automatic Linux binary management.

---

## 🚀 Local Getting Started (Optional)

### 1. Prerequisites
Ensure you have the following installed on your local system:
- Python 3.10 or higher
- Git

### 2. Installation & Setup

Clone the repository to your local machine:
```bash
git clone https://github.com
cd your-repo-name
```

Create a virtual environment and activate it:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install the required Python application modules:
```bash
pip install -r requirements.txt
```

### 3. System Dependency (Only if using pdf2image)
If your version of the application processes PDFs via image conversion (`pdf2image`), you must install **Poppler** on your system:
- **Windows:** Download Poppler, extract it, and add the path to the binary folder inside your app configuration.
- **Mac:** Run `brew install poppler`
- **Linux/Ubuntu:** Run `sudo apt-get install poppler-utils`

*(Note: If your code uses the pure-Python `pypdf` text extraction approach, you can skip this step entirely!)*

### 4. Configuration

Create a `.env` file in the root directory of your project:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Running the Application Locally

Launch the Streamlit server from your terminal:
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501` to use the application.

---

## 🛠️ Project Structure

```text
├── app.py               # Main Streamlit application script
├── requirements.txt     # Python application dependencies
├── packages.txt         # System-level dependencies for Linux hosting environments
├── .env                 # Environment variables configuration file (Local only)
└── README.md            # Project documentation file
```

---

## 🌐 Production Cloud Architecture

This repository is continuously deployed to **Streamlit Community Cloud**:

- **System Packages:** The `packages.txt` file ensures that the cloud Linux server automatically provisions `poppler-utils` during runtime setup.
- **Secrets Management:** The application key **`GOOGLE_API_KEY`** is kept securely isolated out of public source control by injecting it directly through the Streamlit Advanced Settings environment panel.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
