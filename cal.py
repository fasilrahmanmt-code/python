a=int(input("enter first number"))
op=input("enter the opertaion(+,-,/,*)")
b=int(input("enter second number"))

if op=="+":
    print(a+b)

elif op=="-":
    print(a-b)

elif op=="*":
    print(a*b)

elif op=="/":
    if b!=0:
      print(a/b)
    else:
      print("cannot dividec by zero")

else:
 print("Invalid operation")