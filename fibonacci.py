'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
num=int(input("enter the value till which you want to run the series:"))
temp=0
b=1
s=0
i=1
while (i<=num):
    print(s)
    i=1+i
    temp=b
    b=s
    s=temp+b
