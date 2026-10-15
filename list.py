"""list-is a collection of items that are ordered,changebale and allows duplictad eleemments """

list_1=[1,2,3,4,5,"banana","python"]
print(list_1)

# accessing

print(list_1[-2])
print(list_1[4])

print(list_1[2:8])

# change list items -list are mutable 

l=[1,2,3,4,5]
l[1:3]=['a','b']
print(l)

# append() - add an item to end to list
list=['apple','banana','orange']
list.append('mango')
print(list)

# insert()- inser an item at a specific indx
list1=['aplle','mango']
list1.insert(1,'orange')
print(list1)

# extend()-add element from nother list

list_11=['car','swift','zen']
list_22=['bike','fz','rx']
list_11.extend(list_22)
print(list_11)

#  

car=['bmw','benz','audi']
car.extend(['duke','bullet','himalaya'])
print(car)

# remove item from a list

# remove() -remove the first occurence of a specified item
fruit=['banana','apple','mango']
fruit.remove("banana")
print(fruit)

# pop- remove an item at the specified index and return it if no index is specied , it remove last item

names=['fasil',1,'sanjay']
popped=names.pop(2)
print(popped)

# del -- delete an item at a specific index or delte the entire list

a=['car','bike','ship']
del a[2]
print(a)

# clear- empties the entire list

b=['sanjay','kohli','dhoni']
b.clear()
print(b)


# list methods
# python built in methods

# count() return the number of occurence of a specific value


ab=[1,22,33,4,4,5,6,6,7,42]
print(ab.count(4))

# index- return the index of the first occurence 

flist=['a','b','c','b']
print(flist.index('b'))

# reverse-reverse the order of the list

og=[1,2,3,4,5,6,6,77,7]
og.reverse()
print(og)

# sort():sorts the list in asceding order

number=[3,325,2,53,2,2,32,66,734,5,6336]
number.sort()
print(number)


# descendng order
num=[39,44,552,124,52,66,2,6,3,7,33,66,]
num.sort(reverse=True)
print(num)

#  copy()-return a shallow copy of thelist

org=[1,2,3]
copied=org.copy()
print(copied)

copy=org[:]
print(copy)

# joinig list- using + opertaor or extend

clg=['gems','majlis','safa']
uni=['calicut','kannur','kerala']
join=clg+uni
print(join)



