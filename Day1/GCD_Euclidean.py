a=10
b=20

while(a>0 and b>0):
    if(a>b):
        a=a%b
    else:
        b=b%a

if(a==0):
    print(b)

if(b==0):
    print(a)

#lcm =  (Product of two numbers) / GCD