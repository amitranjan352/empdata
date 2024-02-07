'''a =4
b=10
if a>b:
    print("yes")
else:
    print("no")

num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)

def simple_interst(p,r,t):
    print("the principal",p)
    print("rate of interest",r)
    print("time of period",t)
    si=(p*r*t/100)
    print("simple interest is =",si)
    return si
simple_interst(8,6,5)'''

# p = int(input("enter a principal:"))
# r = int(input("enter a rate of interest:"))
# t =int(input("enter a time of peroid:"))
# si=(p*r*t/100)
# print("simple interest of number:", si)

p =int(input("enter a principal:"))
r =int(input("enter a rate:"))
t =int(input("enter a time:"))
a=p*(1+(r/100))**t
ci=a-p
print("compound interest :",ci)




