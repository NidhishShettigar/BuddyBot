from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Generative AI API
genai.configure(api_key="AIzaSyABaX1HoYvWBXg77ZYqo2gGhqHVzzj098Q")

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_route():
    data = request.get_json()
    user_message = data.get('message', '')

    try:
        # Send user message to generative AI and get response
        response = chat.send_message(user_message)
        reply = response.text

        return jsonify({'reply': reply})

    except Exception as e:
        return jsonify({'reply': f"Sorry, an error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True) 