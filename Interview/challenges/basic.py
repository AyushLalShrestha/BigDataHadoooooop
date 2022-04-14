

# Lambda functions: Question 2
def multipliers():
    return [lambda x : i * x for i in range(4)]
print([m(2) for m in multipliers()])


# pyt2 and 3
def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y))

div1(5, 2)
div1(5., 2)
div2(5, 2) 
div2(5., 2.)


# List slicing
list = ['a', 'b', 'c', 'd', 'e'] 
print(list[10:])




# Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
# (a) even numbers, and
# (b) from elements in the original list that had even indices 
list_one = [1, 3, 2, 6, 5, 7]
list_two = [x for x in list_one[::2] if x%2 == 0]
list_two = list(filter(lambda x: x % 2 == 0), list_one)

# Dunder method (Will the code below work? Why or why not? )
class DefaultDict(dict):
    def __missing__(self, key): 
        return [] 
d = DefaultDict()
d['florp'] = 127


# async IO: how would you unittest the following code
async def logs(cont, name):
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock") 
    async with aiohttp.ClientSession(connector=conn) as session: 
        async with session.get(f"http://xx/containers/{cont}/logs?follow=1&stdout=1") as resp: 
            async for line in resp.content:
                print(name, line)

