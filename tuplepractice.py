# 1. Create a tuple 1,2,3,4 and access the element 3 using indexing.

a=(1,2,3,4)
print(a[2])
# output=3
# 2. Convert the tuple 10,20,30 into a list.

t1=(10,20,30)
temp=list(t1)
print(temp)
# output=[10, 20, 30]

# 3. Convert the list 1,2,3 into a tuple.

l1=[1,2,3]
tempt=tuple(l1)
print(tempt)
# output=(1, 2, 3)

# 4. From the tuple ("a","b","c","d") , extract ("b","c") using slicing.

b=("a","b","c","d")
print(b[1:3])
# output=('b', 'c')

# 5. Check if "x" exists inside the tuple ("x","y","z") .

c=("x","y","z")
print("x" in c)
# output=True

# 6. Given 5,3,9,1 , find the maximum value using a tuple function.

c=(5,3,9,1)
print(max(c))
# output=9

# 7. Given 1,2,3 , create a new tuple 1,2,3,1,2,3 using tuple operations only.

d=(1,2,3)
new=d*2
print(new)
# output=(1, 2, 3, 1, 2, 3)

# 8. Count how many times 2 appears in 1,2,2,3,2 using a tuple method

a1=(1,2,2,3,2)
print(a1.count(2))
# output=3

# 9. Find the index of "cat" in ("dog","cat","mouse") .

a2=("dog","cat","mouse")
print(a2.index("cat"))
# output=1

# 10. Reverse 1,2,3,4,5 using slicing.

b1=(1,2,3,4,5)
print(b1[::-1])
# output=(5, 4, 3, 2, 1)

# 11. Combine 1,2 and 3,4 into 1,2,3,4 using tuple operations.

b2=(1,2)
b3=(3,4)
result=b2+b3
print(result)
# output=(1, 2, 3, 4)


# 12. Convert "hello" into a tuple of characters.
text="hello"
tup=tuple(text)
print(tup)
# output=('h', 'e', 'l', 'l', 'o')

# 13. Convert 1,2,3,4 into the list 1,4 by extracting only first & last elements.

li=(1,2,3,4)
# li=list(tup)
rt=li[0],li[-1]
print(list(rt))

# output=[1, 4]

# 14. Given a tuple 10,20,30,40 , replace the value → modify → convert back).

tup1=(10,20,30,40)
temp_list=list(tup1)
temp_list[2]=99
print(tuple(temp_list))
# output=(10, 20, 99, 40)

# 15. Using unpacking, extract a=1 , b=2 , c=3 from 1,2,3 

z=(1,2,3)
(a,b,c)=z
print(a)
# output=1
print(b)
# output=2
print(c)
# output=3

# 16. Create a nested tuple: turn 1,2,3 into 1,2,3, .

tuple1=(1,2,3)
nested=(tuple1,)
print(nested)
output=((1, 2, 3),)

# 17. Merge ("a","b") with ["c","d"] to get a single tuple ("a","b","c","d") (hint: convert list  tuple).

t2=("a","b")
l2=["c","d"]
t3=t2+tuple(l2)
print(t3)
output=('a', 'b', 'c', 'd')

# 18. Check if tuple 1,2,3 is equal to its reverse.

q=(1,2,3)
print(q==q[::-1])
# output=False


# 19. Convert a tuple of lists 1,2,3,4 into a single flat list 1,2,3,4 .

t=([1,2],[3,4])
r = list(t[0] + t[1])
print(r)
# output=[1, 2, 3, 4]

# 20. Given 1, 2,3, 4 , add 5 inside the inner list so result becomes 1, 2,3,5, 4 .

p=(1,[2,3],4)
p[1].append(5)
print(p)

# output=(1, [2, 3, 5], 4)