'''a=10
b=45
try:
    c=(a+b)
    print(c)
except Exception:
    print("zero division number")

a=10
b=50
try:
    if a>b
except Exception:
    print("syntax error")

finally:
    print("value")'''

# str1= "amit kumar"
# str2="my name is {}"
# print(str2.format(str1))


'''str="chandra"
count= {}
for i in str:
    if i in count:
        count[i] +=1
    else:
        count[i] =1
        
print(count)
try:
    a = int(input("enter a first number :"))
    b =int(input("enter a second number :"))
    c= (a/b)
    print("division a and b",c)
except:
    print("zero dicision error")
else:
    print("program excuted")
finally:
    print("na hm me na tum me man marzi")
try:
    a="amit"
    b="10"
    c=(a+b)
    print(c)
except:
    print("typerror")
else:
    print("program excuted")
finally:
    print("excuted")
a=[1,3,"amit",56,89,67]
print(a[0:10])
try:
    a =2300
    if a>2500:
        print("print the value")
except:
    print("syntax error")
else:
    print("submit")
finally:
    print("also submited")

a=input("enter a name:")
print("string lengh is :",len(a))

str1="amit$ kumar$"
print(str1.count("$"))

mark =int(input("enter a mark:"))
if(mark >=90):
    print("grade a")
elif(mark <= 90 and mark >=80):
    print("grade b")
elif(mark <=80 and mark >70):
    print("grade c")
elif(mark <=70 and mark >60):
    print("grade d")
else:
    print("fail")

x =int(input("enter a number:"))
if(x%2==0):
    print("even")
else:
    ("odd")

y=int(input("enter a number:"))
if(y%7==0):
    print("multiply")
else:
    print("not multiply")

a = int(input("enter a first number:"))
b= int(input("enter a second  number:"))
c= int(input("enter a third number:"))

if (a>b and a>c):
    print("a greater than b")
elif(b>a and b>c):
    print("b is grster than a")
elif(c>a and c>b):
    print("c greater than b")
else:
    print("nothing")
try:
    user =input("enter a three fav movies")
    a=[]
    print(user[a])
except:
    print("typeerror")


movies =[]
user1=input("enter a fist fav movies:")
user2=input("enter a second fav movies:")
user3=input("enter a third fav movies:")
movies.append(user1)
movies.append(user2)
movies.append(user3)
print(movies)

x=("a","b","a","b","a","c","a")
print(x.count("a"))

y=["A","C","B","D"]
y.sort()
print(y)

dic ={
    "cat":"small pet animal",
    "table":["a group of frutiure","frutuor group"]

}
print(dic)

d ={
    "1":"amit",
    "2":"duruv",
    "3":"bhulan"
}
print(d.items())

d1 ={
    0: 10, 1: 20


}
d1[2]=30
print(d1)

dic2={1:10, 2:20}
dic3={3:30, 4:40}
dic4={5:50,6:60}
d5={}
for i in(dic2,dic3,dic4):
    d5.update(i)
    print(i)

x=1
while x<=100:
    print(x)
    x +=1
y = 100
while y>=1:
    print(y)
    y -=1
n= int(input("enter a number:"))
i=1
while i<=10:
    print(n*i)
    i+=1


x=[10,20,30,40,50,60,70]
while 

class Animal:
    def __init__(self,bark,run):
        self.bark =bark
        self.run=run
    def value(self):
        print(self.run,self.bark)

v1=Animal("bark","run")
v1.value()'''

class Student:
    def __init__(self):
        self.name="Amit"
        self.roll= 2
        self. passw="amit@234"

    def __init__(self):
        self.name="Amit"
        self.roll= 21
       
    def talk(self):
        print("my name is:",self.name)
        print("my roll number is:",self.roll)
        print("my email id is:",self.passw)

    def pas(self):
        print("my name is amit:",self.name)
        print("my roll roll is :",self.roll)
s=Student()
s.talk()
print(s.name)
print(s.passw)
print(s.roll)


        






    








