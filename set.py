# creating

set1={1,2,3,4}
print(set1)

# also

set2=set([5,6,7,8])
print(set2)

# to create empty set

emptyset=set()
print(emptyset)

# . Accessing Set Items 
# Since sets are unordered, you cannot access items using indexing or 
# slicing. You can, however, iterate through the items in a set using a 
# for loop. 
# can check with membership operator

# add a single item
m1={1,2,3}
m1.add(5)
print(m1)

## update()=> add  multiple item

m2={3,4,5,6}
m2.update([7,8,9])
print(m2)

# remove();Removes the specified element. If the element is not found, it raises a KeyError. 

s1={1,2,3,4}
s1.remove(4)
# s1.remove(6)=>it wil be error
print(s1)

# discard=> Removes the specified element. If the element is not found, it does not raise an error. 

s2={2,4,6,8,10}
s2.discard(5)
print(s2)

#  copy(): Returns a shallow copy of the set. 
set1 = {1, 2, 3} 
set2 = set1.copy() 
print(set2) 

# pop=>Removes and returns a random item from the set since sets are unordered.
my_set = {1, 2, 3, 4} 
removed_item = my_set.pop() 
print(removed_item)  # Output: Random item (e.g., 1) 

# clear(): Removes all items from the set. 
my_set = {1, 2, 3} 
my_set.clear() 
print(my_set)  # Output: set() 

# joining

#1. union(): Returns a new set containing all items from both sets (duplicates removed)

set3={1,2,3}
set4={3,4,5}
unionset=set3.union(set4)
print(unionset)

# Set Intersection (&): Returns the common elements between two sets. 

set1 = {1, 2, 3} 
set2 = {2, 3, 4} 
result = set1 & set2 
print(result) 

# Set Difference (-): Returns the items present in the first set but not in the second.
set1 = {1, 2, 3} 
set2 = {2, 3, 4} 
result = set1 - set2 
print("setdifference",result) 

#  Set Symmetric Difference (^): Returns items that are present in either set but not in both. 

set1 = {1, 2, 3} 
set2 = {2, 3, 4} 
result = set1 ^ set2 
print(result) 

# issubset(set): Returns True if all elements of the calling set are present in the other set. 
set1 = {1, 2} 
set2 = {1, 2, 3, 4} 
print(set1.issubset(set2)) 

# issuperset(set): Returns True if all elements of the other set are present in the calling set. 
set1={1,2,3}
set2={1,2,3,4,5,6}
print(set2.issuperset(set1))

# frozen set =>A frozenset is an immutable version of a set. Once created, you cannot add or remove elements from a frozenset. 
my_frozenset = frozenset([1, 2, 3, 4]) 
print(my_frozenset)  

# Frozensets are useful when you need a collection of unique elements 
# that should not be modified.