letter = '''Dera <|NAME|>,
Greeting from ABC coding house. I am happy to tell about Your Selected!
Have a greate day ahead!
Thanks and Regards,
BilloT
Date: <|DATE|>
'''
name = input("Enter Your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)