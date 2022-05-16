time = input()

rest = str(time[1]+":"+time[2])
if "PM" in time:
        time = time.split(":")
        hour = int(time[0])
        if hour != 12:
            hour += 12
        rest = str(time[1]+":"+time[2])
        if hour <= 9:
            result = str(0)+str(hour)+":"+rest
            final = result[:-2]
        else:
            result = str(hour)+":"+rest
            final = result[:-2]
else:
        time = time.split(":")
        hour = int(time[0])
        rest = str(time[1]+":"+time[2])
        if hour == 12:
            hour = 0
        if hour <= 9:
                result = str(0)+str(hour)+":"+rest
                final = result[:-2]
        else:
                result = str(hour)+":"+rest
                final = result[:-2]
             
print(final)