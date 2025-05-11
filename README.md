# ZC-Project-Rima
![Screenshot 2025-05-10 223112](https://github.com/user-attachments/assets/64abc02d-0b0a-4f33-8e78-971b3c840f1a)

# Project Rima

**Project Rima** is a lightweight LLM-based chatbot built to handle frequently asked questions related to **Zewail City** admissions and registrar services. This alpha version focuses on **textual interaction** using a locally trained model, and is deployed using **Flask** for basic web-based communication.

## 🔍 Overview

This phase includes:
- A lightweight LLM trained on curated FAQs about admissions and registrar topics.
- A basic Flask-based web interface for interacting with the model.
- Text-only interaction (future plans include voice and visual support).
- Hosted and tested as a development prototype.

## 🚀 Future Vision

The future release will expand on this foundation by adding:
- **Voice interaction** via speech-to-text (STT) and text-to-speech (TTS) modules.
- **Visual integration** into an info-desk kiosk or web dashboard.
- Real-time data sourcing from Zewail City's registrar system or official APIs.

## 📁 Project Structure

- `Deep_Learning_Bonus_Zewailcity_Admission_chatbot.ipynb`: Development notebook with data prep, model training, and chat logic.
- `app.py`: Flask application serving the chatbot.
- `README.md`: Project documentation.
- [Upcoming additions]
  - Trained model weights file
  - Voice integration modules
  - Docker setup for deployment

## 🧠 Technologies Used

- Python 3.x
- Flask (for deployment)
- TensorFlow / Keras
- NLP (tokenization, classification)
- Pandas & Numpy
- Jupyter Notebook (for development and testing)

## ⚠️ Current Status

- Version: **Alpha**
- Interaction Mode: **Text-only**
- Deployment: **Local Flask server**
- Not production-ready
- Accuracy is limited to the scope of the training data

## 📌 How to Run

1. Make sure required Python packages are installed (see `requirements.txt` if available).
2. Launch the Flask server:
   ```bash
   python app.py
## 📄 License

Project Rima is released for **educational, academic, and internal prototyping purposes only**. 

Any **commercial use**, **institutional deployment**, or **integration into production systems** — including but not limited to info desks, registrar tools, or university platforms — **requires a formal license agreement and purchase**.

Unauthorized use in a deployed environment, modification for resale, or redistribution of the model or system components is strictly prohibited.

For licensing inquiries, partnership requests, or deployment permissions, please contact the project owner.
