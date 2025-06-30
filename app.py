from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Dummy databases
users_db = [
    {"id": "admin", "name": "Admin User", "email": "admin@company.com", "role": "admin", "password": "admin123", "status": "active"},
    {"id": "emp001", "name": "John Doe", "email": "john@company.com", "role": "employee", "password": "emp123", "status": "active"},
]

events_db = []

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = next((u for u in users_db if u['id'] == data.get('employeeId') and u['password'] == data.get('password')), None)
    if user:
        return jsonify({"message": "Login successful", "user": user}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/api/events', methods=['GET', 'POST'])
def events():
    if request.method == 'GET':
        return jsonify(events_db)
    else:
        event = request.json
        event['id'] = len(events_db) + 1
        events_db.append(event)
        return jsonify(event), 201

# Serve frontend
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# This code is a simple Flask application that serves as a backend for a web application.
# It includes endpoints for user login and event management, and serves static files for the frontend.