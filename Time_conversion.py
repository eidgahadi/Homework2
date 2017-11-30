time = input().split(":")
hours = int(time[0])
minutes = time[1]
seconds = time[2][:2]
ap = time[2][2:]

if ap == "PM" and hours != 12:
    hours += 12
elif ap == "PM" and hours == 12:
    hours = 12
elif ap == "AM" and hours == 12:
    hours = 0

if hours < 10:
    hourString = "0" + str(hours)
else:
    hourString = str(hours)

print(hourString + ":" + minutes + ":" + seconds)