text = input("Enter the text\n")

if("Make a lot of money"in text ):
    spam = True
elif("Buy Now" in text):
    spam = True
elif("Click this" in text):
    spam = True
elif("Subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")

