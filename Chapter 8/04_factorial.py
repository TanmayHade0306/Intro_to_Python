#n! = 1 * 2 * 3 * 4...*n
#n! = [1 * 2 * 3 * 4...n-1] *n
#n! = n * (n-1)!

#n = 7
#product = 1
#for i in range(n):
#    product = product * (i+1)
#print(product)

def factrial_item(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return(product)

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

#f = factrial_item(6)

f = factorial_recursive(9)
print(f)
