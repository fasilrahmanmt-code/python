str="hello world"

"""strring methods"""

# 1-slicing

a="hello python"

print(a[0:5])
print(a[5:13])
print(a[5:0])
print(a[-6:-1]) # negative slicing
print(a[::-1]) # string reevrse
print(a[0:13:2])  #skiping characters

# modifiying string

s="hello world"
new=s.replace("world","python")
print(s)
print(new)


# uppercase and lowercas

name="Fasil rahman"
print(name)
print(name.upper())
print(name.lower())
print(name.title())


# concatenation

s1="f"
s2="r"

print(s1+" "+s2)


# join 

words=["python" , "is", "good"]
sentence=" ".join(words)
print(sentence)

# f-String 
name="fasil"
age=21
place="malappuram"
print(f"My name is {name} and iam {age}year old my place is {place}")


# Escape characters 

# \n -new license
print("hello\nworld")
# \t - tab space
print("hello\t world")
# \''- 
print ('he said , "python is amazing"')

# strinf methods

# len()- return lenght
name="fasil rahman mt"
print(len(name))


# strip()- first and last  remove white splace
print(name.strip())
print(name.lstrip())
print(name.rstrip())

# split()-to split
print(name.split())

# find()
print(name.find("ra"))

# count()
print(name.count("a"))

print(name.startswith("fa"))
print(name.endswith("t"))