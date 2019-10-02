# start to end and end to start 
'''
print("Enter two numbers")
s=int(input())
e=int(input())

if s<e:
      
        for s in range(s,e,1):
            print(s)
            s+=1

else :
    for s in range(s,-e,-1):
         print (s)
         s-=1
'''



# odd nos between 1 to 50
''' 
for i in range (1,51,1):
    print


'''
# table 
'''
a=int(input("Enter a"))
for i in range (1,11,1):
    print (a,"X",i,"="a*i)

'''


# factorial
'''
print("Enter  number")
a=int(input())
fact=1
for i in range(a,1,-1):
            fact*=i
            print(fact)
'''

# factorial
'''
a=int(input("Enter length"))
    print factorial(a)
 '''   

#  power of no  without exponent,  no and power from user
'''
x=float(input("Enter x"))
n=int(input("Ente y"))
p=1

for i in range(n):
        p*=x
print(x,"rest to",n,"is",p)
'''


#  sum of 10 code
'''
a=1
b=9
for i in range(10):
                print(a,"+",b,"=",a+b)
                a+=1
                b-=1
'''


# find sum of n numbers till user enters -1  ,   most imp infosys interview
'''
sum=0

while True:
    n=int(input("Enter no: "))
    if n==-1:
        break
        
    sum+=n
print("sum is " ,sum)
'''
