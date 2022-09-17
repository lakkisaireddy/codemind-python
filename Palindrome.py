N=int(input())
T = N
rev=0
while N>0:
    R=N%10
    rev=rev*10+R
    N=N//10
if T==rev:
    print('True')
else:
    print('False')