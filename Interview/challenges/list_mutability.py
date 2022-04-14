
# List default argument
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

# What will be printed if we print list1, list2 & list3
"""
print(f"list1:  {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
"""