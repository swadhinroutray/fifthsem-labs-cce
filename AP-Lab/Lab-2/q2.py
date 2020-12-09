r1 = int(input("Input Num of rows of M1"))
c1 = int(input("Input Num of columns of M1"))
r2 = int(input("Input Num of rows of M2"))
c2 = int(input("Input Num of columns of M2"))
d1 ={}
d2 ={}
for i in range(r1):
    for j in range(c1):
        x =int(input("Enter element: "))
        if(x==0):
            continue
        d1[i,j] = x

for i in range(r2):
    for j in range(c2):
        x =int(input("Enter element: "))
        if(x==0):
            continue
        d2[i,j] = x

print(d1)
print(d2)
d3 ={}
for i in range(r1):
    for j in range(c1):
        if (i,j) in d1.keys() and(i,j) in d2.keys():
            d3[i,j] = d1[i,j] + d2[i,j]
        elif (i,j) in d1.keys() and (i,j) not in d2.keys():
            d3[i,j] = d1[i,j] 
        elif (i,j) in d2.keys() and (i,j) not in d1.keys():
            d3[i,j] = d2[i,j] 
        else:
            d3[i,j] = 0


for i in range(r1):
    for j in range(c1):
        print(d3[i,j], end =" ")
    print()