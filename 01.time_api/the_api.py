from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__) 

# Define a route to get the current time
@app.route('/get-current-time', methods=['POST'])
def get_current_time():
	# Validate the API key
	api_key = request.headers.get('Authorization')
	if api_key != '12345': 
		return jsonify({"error": "Unauthorized"}), 401 

	# Get and format the current time
	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	# Return the time in JSON format
	return jsonify({"currentTime": current_time}), 200 

if __name__ == '__main__':
	app.run(port=5000, debug=True) 
