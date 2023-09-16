'''N=int(input("Enter a number"))
i=1 
while(i>0 and i<21):
   print(N,'*',i,'=',N*i)
   i=i+1'''

'''X,Y=map(int,input().split())
#X=int(input())
#Y=int(input())
N=int(input())
i=X+1
while(i<=Y):
 if(i%N==0):
    print(i,'num is divisible by N')
    i=i+1'''

'''N=int(input())
while(N!=0):
   sum=sum+
   N=N//10
    
print(sum)'''


'''N=int(input())
x=0
i=0
i_1=0
while(N!=-999):
    x=int(input())
    t=x%N
    if (t==0):
        i=i+1
    else:
        i_1=i_1+1
print(i)
print(i_1)'''


'''N=(input("enter the number:"))
r=len(N)
left=0
right=r-1
while left<right:
  if N[left]==N[right]:
    print("palidrome")
    left=left+1
    right-=r-1
  else:
    print("not palidrome")'''



'''N=int(input())
t=len(N)

while N-1<N+1:
   if N-1==N+1:
     print('palidrome')
     N=t-1
     N=N+1 
   else:
    print("not palidrome")'''



'''n1=0
n2=1
print(n1,n2)+
i=1
while( i>1 and i<1001):
    n3=n1+n2
    n2=n3
    n1=n2
    i+=1'''


'''N=int(input())
i=1
while(2<i<N):
    if(N%i==0):
        print("not prime")
        break
    else:
        print("prime")
else:
    print("not prime")'''


'''sentence=input()
i=0
cap,small,dig,sp=0,0,0,0
while(i<len(sentence)):
    if sentence[i]>='A' and sentence[i]<='Z':
        cap+=1
    elif ord(sentence[i]) >= 48 and ord(sentence[i]) <= 57:
        dig+=1
    elif ord(sentence[i]) >= 97 and ord(sentence[i]) <= 122:
        small+=1
    else:
        sp+=1
    i+=1
print("Capital Count: ",cap)
print("",small)
print("",dig)
print("",sp)'''


'''a=int(input())
b=int(input())
c=int(input())
#Eqn=a*x*x+b*x+c
D=b*b-4*a*c
x_1=(-b+D**(0.5))/2*a
x_2=(-b-D**(0.5))/2*a
i=0
while(i>=0):
  if(D>=0):
    print((x_1,x_2))
  elif(D<0):
    print('imaginary roots')
    i+=1'''
    





        

    





    


