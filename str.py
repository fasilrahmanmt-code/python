# 1.Create a string "hello "and convert it to uppercase using a string method.

str="hello"
print(str.upper())
# output : HELLO

# 2.Given "PYTHON" convert it to lowercase using a string method.

s="PYTHON"
print(s.lower())
# output : python

# 3. from "hello world", replace "world" with "python"using a string method.
str1="hello world"
print(str1.replace("world" , "python"))
# output:hello python

# 4. Extract "ell"  from "hello" using slicing only

str2="hello"
print(str2[1:5])
# output:ello

# 5.Reverse the string "python" using slicing (no loops).

str3="python"
print(str3[::-1])
# output:nohtyp

# 6.Combine "hello" and "world" into one string using string operations.

s1="hello"
s2="world"
s3=s1+" "+s2
print(s3)
# output:hello world

# 7. Repeat the string "hi" to get "hihihi" using string operations

text="hi"
print(text*3)
# output:hihihi

# 8.Check if "cat" exists in "concatenate" using a string operator.

print("cat" in "concatenate")
# output:True

# 9.Count how many times "a" appears in "banana" using a string method.

str4="banana"
print(str4.count("a"))
# output:3

# 10. Remove leading and trailing spaces from " hello "using a string method.

str5=" hello "
print(str5.strip())
# output:hello

# 11.  find the index of "o" in "hello" using a string method.

str6="hello"
print(str6.find("o"))
# output:4

# 12. Split the string "a,b,c,d" into a list using a string method.

a="a,b,c,d"
print(a.split(","))
# output:['a', 'b', 'c', 'd']

# 13. Join the list ["a","b","c"]into "abc" using a string method.

list=["a","b","c"]
result="".join(list)
print(result)
# output:abc

# 14.Extract every 2nd character from "abcdef" using slicing →expected "ace"

str7="abcdef"
print(str7[::2])
# output:ace

# 15.Replace all "a"with "@"in "banana" using a string method.

str8="banana"
print(str8.replace("a","@"))
# output:b@n@n@

# 16.Check if "hello123" is alphanumeric using a string method.

# 17. Capitalize the first letter of "python"  using a string method

str9="python"
print(str9.title())
# output:Python

# 18:Convert "hello world"into "Hello World" using a string method.

txt1="hello world"
print(txt1.title())
# output:Hello World

# 19. Remove all vowels from "python" using string operations (no loops if possible 😈).

txt2="python"
vowels=txt2.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(vowels)
# output:pythn

# 20.Check if "madam" is a palindrome using slicing.

str_1="madam"
print(str_1[::-1])
# output:madam