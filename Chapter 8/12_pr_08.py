def multi(num):
    count = 1
    while count<=10:
        num = num * 1
        print(num , 'X', count,"=", num * count)
        return count += 1
        
a = 3
b = multi(a)
print(b)
