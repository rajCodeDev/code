import re
Email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w+{2,3}$"
user_Email=input('Enter your email:')

if re.search(Email_condition,user_Email):
    print("RIGHT EMAIL")
else:
    print("WRONG EMAIL")