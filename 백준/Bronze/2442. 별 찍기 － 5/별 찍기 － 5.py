n =int(input())
now =1
for i in range(1,n+1):
    #(n-1-i)*("#")
    print((n-i)*(" ")+"*"*(now))
    now+=2

