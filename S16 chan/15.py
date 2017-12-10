time = int(input("What's the time in military format? (HHMM) "))

if time >= 0000 and time < 100:
    print(time + 1200, "AM")
elif time >= 100 and time < 1200:
    print(time, "AM")
elif time >= 1200 and time <= 1259:
    print(time, "PM")
else:
    print(time - 1200, "PM")
