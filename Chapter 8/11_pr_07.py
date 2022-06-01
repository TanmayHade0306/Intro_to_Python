def remove_and_split(string, word):
    newStr =  string.replace(word, "")
    return newStr.strip()

this = "     Tanmay is the good     "
n = remove_and_split(this, "")
print(n)
#print(this)
#print(this.strip())