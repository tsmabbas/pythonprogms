

# collection types
# contain elements of one or more data types
# order, mutability

# Lists: ordered, mutable
fruits = ["apple", "orange", "cherry", "banana","grape"]
print(fruits[2])
print(fruits[-3])
print(fruits[1:3])
print(fruits[-3:-1])
print(fruits[:4])
print(fruits[1:])
print(fruits[0:-1:2])
print(fruits[::-1]) # reverse the list


fruits1 = [["apple", "orange", "cherry"], ["banana","grape"]]
print(fruits1[1])

fruits2 = ["apple", "orange", "cherry", "banana","grape"]

fruits2.append('blackcurrent')
fruits2.insert('mango')
fruits2.extend(['blackcurrant', 'strawberry', 'mango'])

print(fruits2)

fruits2.remove("apple") # when value known use remove which remove the first occurence

print(fruits2)

fruits2.pop(3) # when the index known returns value

fruit4 = fruits.pop(3)

del fruits[3] # value not retuned like pop

fruits2[2] = "mango"

print(fruits2)

fruits2.sort()

fruits2.sort(key=len)

fruits2.sort(key=len, reverse=True)

list2 = sorted(fruits2, key=len, reverse=True)

print(fruits2)

list3 = ["apple", "orange", "cherry", "banana","grape","apple", "orange", "cherry",]

print(list3.count("pear"))

list4 = sorted(list3, key=list3.count, reverse=True)

print(ist3)

print(list4.index('grape'))

# find the position of the multiple occurence of the item
def find_all_indexes(l: list) -> list;
    indices =[]
    for i in range(len(l)):
       if l(i) == element:
            indices.append(i)
    return indices


# Tuples: Ordered, immutable

tuple1 = (1, 2, 3, 4, 5)
tuple1 = 1, 2, 3, 4, 5
string1 = "Hello World!"
print(string1[0:5])

string2 = "ABCDE"

a,b,c,d,e = string2

print(c)

tuple1 = "apple", "pear", "cherry"

apple, pear, cherry = tuple1

print (apple)

# Dictionaries: mutable, ordered
# Store association between 2 object as key-value pairs
# Key : Value
cap_cities = {"UK":"London", "France":"Paris", "Italy":"Rome"}
cap_cities2 = dict(Belgium="Brussels", Germany="Berlin", Spain="Madrid")
print(cap_cities)
print(cap_cities2)
print(cap_cities("uk")) #search only by key
print(cap-cities.get("Netherlands", "Not found"))
cap_cities["UK"] = "Manchester"
cap_cities.update(UK="Manchester",France="Marseiles")
cap_cities["Netherlands"] ="Amsterdam"
cap_cities.pop("UK") # return  value
del cap_cities["France"]
print(list(cap_cities.keys()))
print(list(cap_cities.values()))
print(list(cap_cities.items()))

# Sets: unordered, mutable
# no duplicate stored 
# can only contain immutable elements - ie., not lists, sets or dictionaries
set1 = {1,2,3,4,5}
set2 = set()
set2.add("hello")
set2.add("world")
set2.add("first")
set2.remove("hello")
set2.discard("table")

print(set2)



