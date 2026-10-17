tuples=(1,2,3,"fasil",4,5)
print(tuples)

fruit=("apple,")   
# to define a single item in tuble

# accesing
print(tuple[1],tuple[-1])

# slicing
print(tuple[1:-3])
print(tuple[::-1])

# reassigning

tup=(10,20,30,40)
print(tup)

# covert tuple to list

tp1=("suzuki","toyota","tata")
temp_list=list(tp1)
print(temp_list)
temp_list.append("hyundai");
temp_list[2]="benz"
print(temp_list)
tp=tuple(temp_list)
print(tp)


tup=("apple","banana","orange","apple","banana","orange")
(f1,f2,*f3)=tup
print(f1)
print(f2)
print(f3)


tup1=(1,2,3)
tup2=(4,5,6)
join=tup1+tup2
print(join)

# tuple method - only 2

# count
# index

temp=(1,2,2,2,3,34)
print(temp.count(2))
print(temp.index(3))



# you can delete enrire tuple

mtup=('apple', 'banana', 'cherry')
del mtup
print(mtup)  # This would raise an error as the tuple no longer exist


print(dir(tuple))

