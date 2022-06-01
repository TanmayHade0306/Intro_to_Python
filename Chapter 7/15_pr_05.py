i = 0
num = 5
if num < 0:
    print("need positive number")
else:
    sum = 0
    while(num>0):
        sum += num
        num-= 1
    print(sum)