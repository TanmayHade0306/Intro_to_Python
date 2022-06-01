def rec(n):
    if n == 0:
        return 0
    else:
        return n + rec(n-1)

a = 9
b = rec(a)
print(b)