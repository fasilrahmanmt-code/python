# 1. Create a list  1,2,3 and add  4 to the end using a list method.

a=[1,2,3]
a.append(4)
print(a)

# output=[1, 2, 3, 4]

# 2.Given 10,20,30 , remove 20 using a list method.

b=[10,20,30]
b.remove(20)
print(b)

# output=[10, 30]

# 3. From 5,3,9,1 , sort the list in ascending order using a list method.

c=[5,3,9,1]
c.sort()
print(c)

# output=[1, 3, 5, 9]

# 4. From 1,2,3,4,5 , extract  2,3,4 using slicing only.

d=[1,2,3,4,5]
print(d[1:4])

# output=[2, 3, 4]

# 5.. Reverse the list 1,2,3,4 using slicing 

e=[1,2,3,4]
print(e[::-1])

# 6.Combine 1,2 and  3,4 into one list using list operations.

f=[1,2]
g=[3,4]
f.extend(g)
print(f)

# output:[1, 2, 3, 4]

# 7. Convert 7,8 into 7,8,7,8 using list operations.

h=[7,8]
print(h*2)

# output=[7, 8, 7, 8]

# 8. Check if 3 exists in 1,2,3,4 using a list operator.

i=[1,2,3,4]
print(3 in i)

# output=True

# 9.count how many times 2 appears in 1,2,2,3,2 using a list method.

j=[1,2,2,3,2]
print(j.count(2))


# output=3

# 10. Remove the last element from ["a","b","c","d"] using a list method

k=["a","b","c","d"]
print(k.pop())
print(k)

# output= d
# ['a', 'b', 'c']


# 11. Insert "x" at index 1 in ["a","b","c"] using a list method.

l=["a","b","c"]
l.insert(1,"x")
print(l)

# output=['a', 'x', 'b', 'c']

# 12. Replace the element at index 2 in 13. Convert 10,20,30,40 with 99 using indexing

m=[10,20,30,40]
m[2]=99
print(m)

# output=[10, 20, 99, 40]

# 13. convert range(5) into a list using list functions.

n=list(range(5))
print(n)

# output=[0, 1, 2, 3, 4]

# 14. Using slicing, extract every 2nd element from  1,2,3,4,5,6 → expected [2,4,6]

o=[1,2,3,4,5,6]
print(o[1::2])

# output=[2, 4, 6]

# 15. Remove all elements from 1,2,3 using one list method.

p=[1,2,3]
p.clear()
print(p)

# output=[]

# 16. Copy a list 4,5,6 using only list tools (no modules)

q=[4,5,6]
copy=q.copy()
print(copy)

# output=[4, 5, 6]

# 17. Convert 1,2,3 into a nested list 1,2,3 using list operations.

num=[1,2,3]
nested=[num]
print(nested)

# output=[[1, 2, 3]]

# 18. Extend 1,2 with 3,4,5 using a list method.
r=[1,2]
s=[3,4,5]
r.extend(s)
print(r)

# output=[1, 2, 3, 4, 5]

# 19. Using list repetition, create a list  ["hello","hello","hello"] .

t=["hello"]*3
print(t)

# output=['hello', 'hello', 'hello']



# 20. Remove the element at index 2 from  10,20,30,40 using a list method.

list=[10,20,30,40]
list.pop(2)
print(list)
# output=[10, 20, 40]

