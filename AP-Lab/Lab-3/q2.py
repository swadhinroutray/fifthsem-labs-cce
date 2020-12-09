def getUnique(L,n):
    x = set()
    for i in range(n):
        if L[i] not in x:
            x.add(L[i])
    return x    



def main():
    L1 = []
    n = int(input("input size of list: \n"))
    for i in range(n):
        x = int(input("Input a number: "))
        L1.append(x)
    uniqueL =getUnique(L1,n)
    print(uniqueL)


if __name__ == "__main__":
    main()
