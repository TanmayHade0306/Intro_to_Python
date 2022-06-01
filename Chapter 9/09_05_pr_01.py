f = open('poems.txt')
t = f.read()
if 'twinkle'in t:
    print("Twinkle is present")
else:
    print("Twinkel is not present")
f.close()