import garth

# Authenticate with Garmin Connect
client = garth.Client()

# Replace with your actual credentials
email = "ben.l.williams@hotmail.com"
password = "r.J7d%>CJ72CjDW3u7ih?Bk&"

client.login(email, password)

# Fetch and print profile info
profile = client.user_profile()
print(profile)
