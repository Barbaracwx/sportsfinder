from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # This allows all domains to access your Flask API

# Load environment variables from .env file
load_dotenv()

# MongoDB URI and database
MONGO_URI = os.getenv("MONGO_URI")  # You can use your Mongo URI here
client = MongoClient(MONGO_URI)
db = client.sportsfinder
users_collection = db.users

@app.route('/save-profile', methods=['POST'])
def save_profile():
    try:
        profile_data = request.json  # Get the data sent by the frontend (in JSON format)
        
        # You can add any validation here for profile_data
        
        # Insert the data into MongoDB
        result = users_collection.insert_one(profile_data)
        
        return jsonify({"message": "Profile saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
