from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import os
import requests

app = Flask(__name__)
CORS(app)

MODEL_DIR = "my_model"
os.makedirs(MODEL_DIR, exist_ok=True)

# Mapping of filenames to their Google Drive file IDs
model_files = {
    "added_tokens.json":        "1J2wvGHp8lqFczSIud0juQut5SgmNlnRV",
    "config.json":              "12geZicb2JpaHsokJ_2_5CYkzbgY_9RkH",
    "generation_config.json":   "1u2-ux35zCWtz0XU96qmID1-0UynK9PWU",
    "model.safetensors":        "1FQsXlW-WpSa-ZQR38PU3rsrQ4R1Y4wEK",
    "special_tokens_map.json":  "1VDKjFzLtfE17gLpE6gEcYrb9Fq9zOlGW",
    "spiece.model":             "12wveM6XBKzGVzvqwON2QgDoXAeviv0DV",
    "tokenizer_config.json":    "1IPUUuMxFalxmWjTrpP3hpz0yzfvY-I95"
}

def download_from_gdrive(file_id, destination):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(url, stream=True)
    if response.status_code == 200 and 'text/html' not in response.headers.get('Content-Type', ''):
        with open(destination, "wb") as f:
            for chunk in response.iter_content(1024 * 1024):
                f.write(chunk)
        print(f"Downloaded: {destination}")
    else:
        print(f"Failed to download {destination}: status {response.status_code}, possibly a Google warning page")

def ensure_model_files():
    for filename, file_id in model_files.items():
        path = os.path.join(MODEL_DIR, filename)
        if not os.path.exists(path):
            print(f"{filename} not found. Downloading...")
            download_from_gdrive(file_id, path)

# Download missing model files
ensure_model_files()

# Load model and tokenizer
print("Loading model and tokenizer...")
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR)
tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST", "GET"])
def chat():
    if request.method == "GET":
        return jsonify({"message": "Welcome to the Chat API 🤖. Please use POST with a 'message'."})

    data = request.get_json(force=True)
    user_input = data.get("message", "")

    if not user_input.strip():
        return jsonify({"response": "Please enter a message to get started. 😊"})

    input_ids = tokenizer.encode(user_input, return_tensors="pt")

    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=100)
        response = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)