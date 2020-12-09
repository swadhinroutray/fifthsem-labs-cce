n = int(input("Input number of strings \t"))

L = []
L2 =[]
c =0
for i in range(n):
    str = input("\nInput a string: ")
    L.append(str)
    if (str[0] == str[len(str)-1]) and len(str)>=2:
        c=c+1
    if(len(str)%2==1):
        L2.append(str)

print("\nCount: ")
print(c)
print("\n Odd length strings \n")
print(L2)