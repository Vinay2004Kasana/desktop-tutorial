'''x=int(input())
y=int(input())
Addition=x+y
Subtraction=x-y
Multiplication=x*y
Division=x/y
print(Addition,Subtraction,Multiplication,Division)'''


'''x=int(input())
y=int(input())
z=int(input())
t=int(input())
avg=(x+y+z+t)/4
print(avg)'''


'''p=int(input("PRINCIPAL-"))
r=int(input("RATE OF INTEREST-"))
t=int(input("TIME-"))
si=(p*r*t)/100
print(si)'''


'''d=int(input("Distance in KM-"))
t=int(input("Time in minutes-"))
speed=d/t
print(speed)'''


'''a=int(input())
b=int(input())
c=int(input())
s=(a+b+c)/2
Area=(s*(s-a)*(s-b)*(s-c))**(0.5)
print(Area)'''



a=int(input())
b=int(input())
c=int(input())
#x=float(input())
#Eqn=a*x*x+b*x+c
D=b*b-4*a*c
x_1=(-b+D**(0.5))/2*a
x_2=(-b-D**(0.5))/2*a
if(D>=0):
    print(x_1,x_2)
elif(D<0):
    print('imaginary roots')






