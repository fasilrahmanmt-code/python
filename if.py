# a=float(input("enter a number:  "))
a=10
if a>0:
    print("positive number")
elif a==0:
    print("zero")
elif a==-2.2:
    print("float")
else:
    print("negative number")


x = 10 
y = 5 
if x > 5: 
 if y < 10: 
  print("x is greater than 5 and y is less than 10") 


# Python's if with and, or, not (Logical Operators) 
#  and: Executes a block if both conditions are true. 
#  or: Executes a block if any one of the conditions is true. 
#  not: Inverts the truth value of a condition. 


x=10
y=10
if x>5 and y<10:
   print("both conditions are true")

if x > 5 or y > 10: 
   print("At least one condition is True") 

if not x < 5: 
    print("x is not less than 5") 


#  Conditional Expressions (Ternary Operator) 
#  Python allows for writing short, one-line if-else statements using 
# the ternary operator. It can be useful for simple conditions.

x = 5 
result = "Greater than 10" if x > 10 else "10 or less" 
print(result) 