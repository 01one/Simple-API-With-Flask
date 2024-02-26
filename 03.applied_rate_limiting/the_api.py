from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import random
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def is_prime_miller_rabin(n, iterations=40):
    """Performs the Miller-Rabin Primality Test to determine if a number is likely prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Decompose n-1 into the form 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(iterations):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Initialize the scheduler
scheduler = BackgroundScheduler()

# Define the users and their limits
users = {"12345": {"limit": 5}, "45365": {"limit": 5}}

# Function to reset the limits
def reset_limits():
    print("Resetting limits...")
    for user_info in users.values():
        user_info["limit"] = 5

# Schedule the job to run every 24 hours
scheduler.add_job(reset_limits, 'interval', hours=24)

# Start the scheduler
scheduler.start()

# Define a route to check if a number is prime
@app.route('/check-prime', methods=['POST'])
def check_prime():
    # Validate the API key
    api_key = request.headers.get('Authorization')
    if api_key not in users:
        return jsonify({"error": "Unauthorized"}), 401

    # Get the number from the request
    limit = users[api_key]['limit']
    if not limit == 0:
        data = request.get_json()
        number_to_test = data.get('number')

        # Check if the number is prime
        is_prime = is_prime_miller_rabin(number_to_test)

        # Update the request limit
        users[api_key]['limit'] -= 1

        # Return the result
        return jsonify({"number": number_to_test, "isPrime": is_prime}), 200
    else:
        return jsonify({"error": "Request limit exceeded. Please try again later."}), 429

if __name__ == '__main__':
    app.run(port=5000, debug=True)
