import garth
import os
from dotenv import load_dotenv
from getpass import getpass

# Load environment variables
load_dotenv()

# Retrieve credentials
email = os.getenv("GARMIN_EMAIL") or input("Enter Garmin email: ")
password = os.getenv("GARMIN_PASSWORD") or getpass("Enter Garmin password: ")

# Session directory
SESSION_DIR = "session.json"

# Attempt to resume session
try:
    garth.resume(SESSION_DIR)
    print("Resumed session from saved tokens.")
except Exception as e:
    print(f"No valid session tokens found. Logging in... ({e})")
    garth.login(email, password)
    garth.save(SESSION_DIR)
    print("Session tokens saved.")

# Initialize client
client = garth.Client()

### ---- FETCH DATA ---- ###

# Fetch raw user profile data
try:
    # Create client instance
    client = garth.Client()

    # Fetch user profile using Garth's provided function
    user_profile = client.user_profile()

    # Print raw JSON response
    print("\nUser Profile Data:")
    print(user_profile)

except Exception as e:
    print(f"Failed to fetch user profile: {e}")
