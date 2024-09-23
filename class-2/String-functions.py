text= "where is San Antonio TX?"
print(text[:5]) # print after 5 
print (text[6:11]) # print 6 to 11 

for x in text:
    print(x)

#string formatting 
name,age ="john",25
print("%s is my name" %name)
print("%d is my age" %age)
print("%s is %d years old" %(name,age))

NEWLINE = "\n"
print(f"{name.lower()} is {age} years old",end=NEWLINE)
print(f"{name.upper()} is {age} years old")

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())
print(text.casefold())

text = "hello world and welcome to python world"
# Count 
print(text.count("world")) # 2 
print(text.count("python")) # 1 

#find 
print(text.find("world")) # 6
print(text.find("python")) # 27

#index 
print(text.index("world")) # 6
print(text.index("python")) # 27 

# Value not found 
txt = "Hello, welcome to my world."

print(txt.find("q")) # -1 
# print(txt.index("q")) # Error 

# Join
names = ['avnit','loves','hockey']
sep= '\n'
print(sep.join(names))

# replace 
output = txt.replace("world","life")
print(output)

# 