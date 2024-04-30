# Big O(1) -- Better than Array's as you don't need to loop linearly

name = {}

name["saed"] = 99
name["ali"] = 22


print(name)

name.pop("saed")

print(name)


---------------------------

saed = {}

saed = {'saed': 2, 'abdi': 9, 99: 'mo'}

isIn = 'saed' in saed

value = saed.value()
index = saed.items()
keys = saed.keys()

print(isIn) #bool
