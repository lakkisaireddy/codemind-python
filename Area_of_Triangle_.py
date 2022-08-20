a,b,c=map(int,input().split())
d=(a+b+c)/2
x=(d-a)**0.5
y=(d-b)**0.5
z=(d-c)**0.5
q=d**0.5
A=x*y*z*q
print("%.2f"%A)