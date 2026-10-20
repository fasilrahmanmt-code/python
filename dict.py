dict1={"name":"fasil","age":22,"place":"moorkkannad"}
another=dict(name="alice",age=24,city="los angles") # useingdict constrictor
print(dict1,another)
empty={}
print(empty)

# accesing

print(dict1["name"])
# get 
print(dict1.get("age"))

# changing items

dict1["age"]=21
dict1["collge"]="gems"
print(dict1)

# adding
dict1["collge"]="gems"
print(dict1)

# removing(pop,popitem(),del,clear())
# pop()
my_dict = {"name": "John", "age": 30, "city": "New York"}
age=my_dict.pop("age")
print(age)
print(my_dict)

# popitem()
my_dict = {"name": "John", "age": 30, "city": "New York"}
last_item=my_dict.popitem()
print(last_item)
print(my_dict)

# del
my_dict = {"name": "John", "age": 30} 
del my_dict["age"]
print(my_dict)

# clear()
my_dict1 = {"name": "John", "age": 30} 
my_dict1.clear()
print(my_dict1)

# copy
og={"name": "John", "age": 30} 
copy_dict=og.copy()
print(copy_dict)

# using dict for copy
org= {"name": "John", "age": 30} 
copyd=dict(org)
print(copyd)

# nested dect

nested_dict={
    "p1":{"name":"john","age":30},
    "p2":{"name":"Alice","age":22}
}
print(nested_dict)
print(nested_dict["p1"]["name"])

# dict ,ethod

# key()

my_dict = {"name": "John", "age": 30} 
print(my_dict.keys())

# values
print(my_dict.values())  # Output: dict_values(['John', 30]) 

# items
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30)]) 

# update
my_dict = {"name": "John", "age": 30} 
my_dict.update({"city": "New York", "age": 31}) 
print(my_dict)  #

# fromkeys()
keys = ["name", "age", "city"] 
new_dict = dict.fromkeys(keys, "Unknown") 
print(new_dict) 

# setdefault(key, value)
my_dict = {"name": "John", "age": 30} 
city = my_dict.setdefault("city", "New York") 
print(city)    