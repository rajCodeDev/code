num1=float(input("Enter the number1:"))
num2=float(input("Enter the number2:"))
operator=input("Enter the operator")


if  operator=='+':
     print(num1+num2)
elif operator=='-':
      print(num1-num2)
elif operator=='*':
      print(num1*num2)
elif operator=='/':
      print(num1/num2)
elif operator=='%':
      print(num1%num2)
else:
      print('invalid')
