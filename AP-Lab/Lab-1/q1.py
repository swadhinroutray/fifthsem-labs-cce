

n = int(input("input size of list 1 \n"))
m = int(input("\ninput size of list 2 \n"))
L1=[]
L2=[]
for i in range(n):
   x = int(input("\nenter item of list 1 \t"))
   L1.append(x)
for i in range(m):
    x = int(input("\nenter item of list 2 \t")) 
    L2.append(x)
L3 =[]
for i in range(n):
    if L1[i]%2 != 0:
        L3.append(L1[i])

for i in range(m):
    if L2[i]%2 == 0:
        L3.append(L2[i])

print(L3)