"""operators"""
# 1-Arithmetic opr

a=20
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)  #floor division
print(a**b)  #power 10^2

# 2-Assignment operators

a=10
a+=10  #a=a+10
b=20
b+=10 #b=b+10
print(b)

a=50
a-=10
a*=10
a/=10
a%=10
a//=10
a**=10

# 3-comparison
a=10
b=20

print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

# 4-Logical opr
# and
a=True
b=False
print(a and b)
# or
print(a or b)
# not

print( not a)

#5- Membership operator
a="fasil"
b=[2,3,4,5,]
print("i" in a)
print(1 in b)
print("lr" not in a)

# 6-identity
a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a in b) # check it in same memory location
print(a is not b)
