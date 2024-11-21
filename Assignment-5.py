def convert_time(hours):
    # Convert hours to minutes
    minutes = hours * 60
    # Convert hours to seconds
    seconds = hours * 3600
    return minutes, seconds

# Prompt the user to enter a time duration in hours
hours = float(input("Enter the time duration in hours: "))

# Convert the time duration to minutes and seconds
minutes, seconds = convert_time(hours)

# Display the converted time duration
print(f"The time duration is: {minutes} minutes or {seconds} seconds.")
