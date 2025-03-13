
# ----------- STRINGS ------------
# sort
s = "racecar"
sorted(s)
# join strings
a = ['Geeks', 'for', 'Geeks']
res = ' '.join(a) # Geeks for Geeks
a = [1, 'apple', 3.14, 'banana']
# Converting list to string using map() function
res = ' '.join(map(str, a)) # 1 apple 3.14 banana
# split
res = (s.split())

# ----------- HASHMAPS ------------
thisdict = {}

# get value (VALUES CANNOT BE LISTS)
# keyname	Required. The keyname of the item you want to return the value from
# value	Optional. A value to return if the specified key does not exist. Default value None
thisdict.get(keyname, value)

# delete items
thisdict.popitem()
del thisdict["model"]
thisdict.clear()

# loop through values or keys
for x in thisdict.values():
  print(x)

for index, key in enumerate(thisdict, start=1):
    print(f"Index: {index}, Key: {key}, Value: {thisdict[key]}")

# copy
mydict = thisdict.copy()

# access nested dict
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# ----------- FREQUENCIES ------------
from collections import Counter  
a = [1, 2, 2, 3, 4, 2, 5, 3, 1]  
b = [1, 2, 3]  
freq = Counter(a)  
res = {x: freq[x] for x in b}  
print(res)  
# Output: {1: 2, 2: 3, 3: 2}

count = {}
for num in nums:
    count[num] = 1 + count.get(num, 0)

# ----------- HEAPS ------------
