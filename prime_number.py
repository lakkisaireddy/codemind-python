a=int(input())
s=0
for i in range(1,a+1):
    if a%i==0:
        s+=i
if s==a+1:
    print('prime')
else:
    print('not a prime')