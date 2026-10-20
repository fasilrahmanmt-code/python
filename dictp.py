# 1.Create a dictionary with keys "name" and "age" and values "Nik" and 20
a={
    "name":"Nik",
    "age":20
}
print(a)

# output={'name': 'Nik', 'age': 20}

# 2. Access the value of key "name" from{"name": "Nik", "age" 20 
a={
    "name":"Nik",
    "age":20
}
print(a["name"])

# output:Nik

# 3. Add a new key "city" with value {"name": "Nik", "age" 20 .
a={
    "name":"Nik",
    "age":20
}
a["city"]="delhi"
print(a)

# output={'name': 'Nik', 'age': 20, 'city': 'delhi'}

# 4. Update the value of "age " to 25 in {"name": "Nik", "age" 20}
a={
    "name":"Nik",
    "age":20
}
a["age"]=25
print(a)

# output={'name': 'Nik', 'age': 25, 'city': 'delhi'}
 
#  5. Delete the key "age" from{"name": "Nik", "age" 20 .
a={
    "name":"Nik",
    "age":20
}
print(a.pop("age"))

# output=25

# 6. Check if the key "email" exists in{"name": "Nik", "age" 20 .
a={
    "name":"Nik",
    "age":20
}

print(a.get("email"))

# output=None

# 7. Get all keys from"Delhi" to25 in{"name": "Nik", "age" 20 using a dictionary method.

a={
    "name":"Nik",
    "age":20
}
print(a.keys())

# output=dict_keys(['name', 'age'])

# 8. Get all values from name": "Nik", "age" 20 using a dictionary method.

a={
    "name":"Nik",
    "age":20
}
print(a.values())

# output=dict_values(['Nik', 20])

# 9. Convert the dictionary{"a" 1, "b" 2 into a list of (
dict_1={
    "a":1,
    "b":2
}

print(dict_1.items())

# output=dict_items([('a', 1), ('b', 2)])

# 10. Create a dictionary from two lists: (use zip method)     keys = ["name", "age"]values = ["Nik", 20 .

keys=["name","age"]
Values=["nik",20]

result=dict(zip(keys,Values))
print(result)

# output={'name': 'nik', 'age': 20}

# 11. Count how many keys are in{"a" 1, "b" 2, "c" 3 .

dict_2={
    "a":1,
    "b":2,
    "c":3
}

print(len(dict_2))

# output=3

# 12. Merge two dictionaries{"a" 1 and {"b" 2 into one. 
a1={"a":1}
b1={"b":2}
a1.update(b1)
print(a1)

# output:{'a': 1, 'b': 2}

# 13 . Clear all elements from{"a" 1, "b" 2 using a dictionary method.

a2={'a': 1, 'b': 2}
a2.clear()
print(a2)
# output={}

# 14. Copy the dictionary{"x" 10, "y" 20 using a dictionary method.

b2={
    "x":10,
    "y":20
    }
dcopy=b2.copy()
print(dcopy)

# output{'x': 10, 'y': 20}

# 15. Get the value of key salary" safely from{"name": "Nik", "age" 20 without getting an error.

a={
    "name":"Nik",
    "age":20
}

print(a.get("salary"))

# output:None

# 16. From{"a" 1, "b" 2, "c" 3 , remove the last inserted item using a dictionary method.

dict_2={
    "a":1,
    "b":2,
    "c":3
}

print(dict_2.popitem())
print(dict_2)

# output:('c', 3)
# {'a': 1, 'b': 2}

# 17. Givenstudent = {"name": "Rahul", "marks": {"math" 90, "science" 85 ,access only the "science" marks.

student={
    "name":"rahul",
    "marks":{"maths":90,"science":85}
}
print(student["marks"]["science"])

# output:85

# 18. From the above student dictionary, update "math" marks to 95 .

student["marks"]["maths"]=95
print(student)

# output={'name': 'rahul', 'marks': {'maths': 95, 'science': 85}}


# 19. Add a new subject "math" marks to 95 ."english" 88 inside the "marks" dictionary.

student["marks"]["english"]=88
print(student)

# output={'name': 'rahul', 'marks': {'maths': 95, 'science': 85, 'english': 88}}

# 20. Delete the subject "science" from inside "marks" .

del student["marks"]["science"]
print(student)

# output={'name': 'rahul', 'marks': {'maths': 95, 'english': 88}}