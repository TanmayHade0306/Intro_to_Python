def percent(marks):
    return((marks[0]+marks[2]+marks[3])/400)*100

marks = [45,78,86,77]
percentage = percent(marks)

marks2 = [75,98,88,78]
percentage2 = percent(marks2)

print(percentage,percentage2)