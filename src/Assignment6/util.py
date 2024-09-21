
from datetime import datetime

def tt():
# Input two timestamps directly
    timestamp1 = "Sat 07 May 2021 12:15:30 +0530"
    timestamp2 = "Sat 08 May 2021 14:30:15 +0000"
# Convert the timestamps to datetime objects using strptime
    datetime1 = datetime.strptime(timestamp1, '%a %d %b %Y %H:%M:%S %z')
    datetime2 = datetime.strptime(timestamp2, '%a %d %b %Y %H:%M:%S %z')
# Calculate the absolute difference between the two timestamps in seconds
    time_difference = abs((datetime1 - datetime2).total_seconds())
# Print the result
    return f"The difference in seconds is: {int(time_difference)} seconds"


print(tt())