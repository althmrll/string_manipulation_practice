#Ask user to input fullname
name= input("Enter your full name:")

#print user's name in pascal case
correct_case= name.lower()
print(correct_case.replace(" ","_"))