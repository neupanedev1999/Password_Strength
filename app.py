from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Function to check password strength
def check_strength(password):
    strength = 0

    # Password should be at least 8 characters long
    if len(password) >= 8:
        strength += 1
    # Should contain uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    # Should contain lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    # Should contain digits
    if re.search(r"[0-9]", password):
        strength += 1
    # Should contain special characters
    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1

    return strength

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password', '')

    strength = check_strength(password)

    # Return the strength score
    return jsonify({'strength': strength})

if __name__ == '__main__':
    app.run(debug=True)
