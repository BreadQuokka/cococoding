n= int(input())
for i in range(n):
    string= input()
    word= string.split()
    for i in word:
        print(i[::-1],end=" ")