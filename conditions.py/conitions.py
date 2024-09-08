a=34
b=39
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a is equal to b")
# else:
#     print('not equal')
# if a<b :print("a is greater than b")
# print("A") if a>b else print("B")
# i=1
# while i<6:
#     print(i)
#     i+=1

# i=0
# while i<6:
#     print(i)
#     i+=1
#     if i ==3:
#      continue
#     print(i)
# fruits=['a','b','c','d']
# # for x in fruits:
# #     if x =='b':
# #         break
# #     print(x)
# FRUITS=['e','f','g']
# for x in fruits:
#     for y in FRUITS:
#         print(x,y)
# def my_function(**kid):
#     print("His last name" + kid ["lname"])
# my_function(fname="Tobias",lname="Refsnes")



# def my_function(country='Norway'):
#     print('my country is ' + country)
# my_function("sweden")
# my_function('Pakistan')
# def my_function(x):
#  pass
# def my_function(x,/):
#     print(x)
# my_function(x=6)
# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)
# x=lambda a : a+10
# print(x(5))
# x=lambda a,b:a*b
# print(x(5,5))
# def my_func(n):
#     return lambda a:a*n
# mydoubler=my_func(5)
# print(mydoubler(33))
# class Person:
#     def __init__(self,name):
#      self.name=name
# p1=Person('jon')
# print(p1.name)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#       print(self.firstname,self.lastname)
# x=Person("j",'dor')
# x.printname()
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.graduationyear=year
#     def welcome(self):
#         print(f'elsef',{self.firstname},{self.lastname}, "to class of self.graduationYear",{self.graduationyear})
# s=Student('jon','afds',34)
# s.welcome()
# mystr='banana'
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+1
#         return x
# myclass =MyNumbers()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=39:
#             self.a+1
#             return 
#         else:
#             raise StopIteration
# myclass =MyNumbers()
# myiter =iter(myclass)
# for x in myiter:
#  print(x)
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def move(self):
#         print('drive')
# class Boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print('fly')
# car1=Car("Ford","mustang")
# boat1=Boat("Ibiza","tour")
# plane1=Plane("aef","fas")
# for x in (car1,boat1,plane1):
#     x.move()
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("move")
# class Car(Vehicle):
#     pass
# class Boat(Vehicle):
#     def move(self):
#         print('Sail!')
# class Plane(Vehicle):
#     def move(self):
#         print('flu')
# car1=Car('Ford','Mustang')
# boat1=Boat('ibizs','bafa')
# plane1=Plane('vafd','adfa')
# for x in (car1,boat1,plane1):
#     print(x.brand)
#     print(x.model)
