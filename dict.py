frequencies=[]


heights={
    4:2.1,
    2:2.4,
    1:2.5,
    4:2.7,
    5:3.0,
    6:3.1,
    2:3.5 
    
}
values=heights.values()
# print("the values are: \n",values)

keys=heights.keys()
# print("the keys are\n",keys)
vlist=[]
klist=[]
for value in values:
    
    vlist.append(value)
print("The list for the values is\n",vlist)

for key in keys:
    klist.append(key)
print("the frequencies are:\n",klist)

# for x,y in heights.items():
#     print(x,y)
items=heights.items()
print(items)