time = int(input())
av_spd = int(input())
fuel = (time*av_spd)/12
result = "{:.3f}".format(fuel)
print(result)