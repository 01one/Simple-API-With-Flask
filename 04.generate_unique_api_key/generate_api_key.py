import secrets
import string
import time

def generate_unique_api_key(length=32):
    """Generate a unique API key using a combination of random characters and timestamp."""
    timestamp = str(int(time.time()))  # Get current timestamp as a string
    alphabet = string.ascii_letters + string.digits
    random_part = ''.join(secrets.choice(alphabet) for _ in range(length - len(timestamp)))
    key = timestamp + random_part
    return key

# Generate a unique API key of length 32
api_key = generate_unique_api_key()
print("unique API key:", api_key)
