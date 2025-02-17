from flask import Flask, request, jsonify
import logging
from bot import handle_profile_data  # Import the function to process the data

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("Received webhook POST request")
        # Get the data sent to this endpoint (expecting JSON)
        data = request.get_json()
        print("Data:", data)
        
        # Log the received data for debugging
        logging.debug("Received Profile Data: %s", data)
        
        # Process the profile data (in bot.py)
        handle_profile_data(data)

        return jsonify({"status": "success", "message": "Profile data received"}), 200

    except Exception as e:
        logging.error(f"Error processing webhook data: {e}")
        return jsonify({"status": "error", "message": "Failed to process data"}), 500

# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
