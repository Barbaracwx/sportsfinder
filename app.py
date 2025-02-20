import os
import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Database Connection
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, sslmode="require")

# API Route to Handle Form Submission
@app.route('/submit', methods=['POST'])
def submit_profile():
    try:
        data = request.get_json()
        chat_id = data.get('chat_id')
        age = data.get('age')
        gender = data.get('gender')
        location = data.get('location')
        sports = data.get('sports')

        if not (chat_id and age and gender and location and sports):
            return jsonify({"error": "Missing required fields"}), 400

        # Connect to DB
        conn = get_db_connection()
        cur = conn.cursor()

        # Insert user profile
        cur.execute("INSERT INTO users (chat_id, age, gender, location) VALUES (%s, %s, %s, %s) RETURNING id",
                    (chat_id, age, gender, location))
        user_id = cur.fetchone()[0]

        # Insert sports preferences
        for sport in sports:
            cur.execute("INSERT INTO user_sports (user_id, sport, skill) VALUES (%s, %s, %s)",
                        (user_id, sport['sport'], sport['skill']))

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Profile submitted successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
