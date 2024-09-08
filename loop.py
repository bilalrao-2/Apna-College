# thislist=['a','b','c']
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1
# thislist=['apple','banana','cherry']
# [print(x)for x in thislist]
# fruits=['apple','banana','cherry','kiwi','mango']
# newlist=[]
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)
# 
# newlist=[x for x in fruits if x!= 'apple']
# print(newlist)
# fruits=['apple','banana','cherry','kiwi','mango']
# newlist=[x for x in range(10)]
# print(newlist)
# newlist=[x.upper()for x in fruits]
# print(newlist)
# newlist=['hello'for x in fruits]
# print(newlist)

# newlist=[x if x!= 'banana'else 'orange'for x in fruits]
# print(newlist)
# fruits=['apple','banana','cherry','kiwi','mango']
# fruits.sort()
# print(fruits)
# thislist=['apple','banana','cherry']
# mylist=thislist.copy()
# print(mylist)
# mylist=list(thislist)
# mylist=thislist[:]
# print(mylist)
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange") 
# thistuple = tuple(y)
# thistuple=tuple(y)
# print(thistuple)
# thistuple=('apple','banana','cherry')
# y=('orange',)
# thistuple+=y
# print(thistuple)
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])
# i = 0

# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 1


# set1={'a','b','c'}
# set2={'d','e','f'}
# set3=set1.intersection_update(set2)
# set4=set1.intersection(set2)
# print(set3)
# print(set4)
thisdic = {
    'brand': 'Ford',
    'model': '2323'
}

# Loop through the dictionary using items()
for  value in thisdic.values():
    print(value)
