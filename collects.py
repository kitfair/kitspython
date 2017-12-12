#Collections
#String: str
#Bytes: bytes
#Array: list
#Dictionary: dict

#1) String: Immutable sequence of unicode codepoints
#Single and double quotes

h = 'This is a string'
print(h)
h = "This is a string"
print(h)

#Multiline string: triple double or single quotes
h = """ this 
is 
a string"""
print(h)

m = "This is\nmulti\nline"
print(m)
m = "This\\"
print(m)

#Raw strings
path = r'C:\User\Documents\book'
print(path)

# String as sequences
s = "parrot"
print(s[3])

#Use the type() function to get the objects type
print(type(s))
print(s.upper())

#Bytes: similar to strings, but is a sequence of unicode points is a sequaence of bytes. Use for raw binary data, fixed width, ASCII

bt = b'data for bytes'

print(bt)
print(bt.split())

#Encode data: utf-8
#l = "Visitamos el zool

#Arrays: A list of mutable objects
#Replace, remove, or append elements
#Delimited by [], and items are separated by commas
l = [1, 2, 3]
print(l)
print(type(l))
a = ["apple", "pear", "orange"]
print(a[1])
b = ["Waldo", 1, 2]
print(b)

ll = ["apple", 1, [1, 2, 3]]
print(ll)

c = ["bear",
     "horse",
     "cat",]
print(c)

#add members

c.append("cow")
print(c)

m = list("Characters")
print(m)
c.insert(1,"pig")
print(c)

#Dictionaries: Mutable mapping of keys to values
#Values are in no order
#{k1: v1, k2: v2, k3: v3}


d = {'alice': "8014443333", 'pedro': "843283248"}
print(type(d))
print(d)


#Access a member
print(d['alice'])
#Update alice
d['alice'] = '842746263'
print(d)

d['maria'] = '848293920'
print(d)

#For loops: visit each items in a series
cities = ["London", "Madrid", "Paris", "Ogden"]
for city in cities:
    print(city)

#Access members of dictionary, a for loop gets the key value
for i in d:
    print(i, d[i])
