import subprocess


# Run the command and capture the output
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# Split the output into lines
data = data.decode('utf-8').split('\n')

# Extract Wi-Fi profile names using list comprehension
profiles = [profile.split(":")[1].strip() for profile in data if "All User Profile" in profile]

# Print header
print("{:<20}| {:}\n".format("Wi-Fi Names", "Passwords"))

for profile in profiles:
    # Run command to get the password for each profile
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
    data = data.decode('utf-8').split('\n')

    # Extract the password
    passwords = [passw.split(":")[1].strip() for passw in data if "Key Content" in passw]

# Print profile name and password
    try:
        print("{:<20}| {}".format(profile, passwords[0]))
    except IndexError:
        print("{:<20}| {:}".format(profile, ""))


