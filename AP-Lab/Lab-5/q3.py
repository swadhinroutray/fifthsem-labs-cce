import itertools

def printSubsets(L,n):
    L1 =[]
    for i in range(n):
        x = list(itertools.combinations(L, i))
        L1.append(x)
    L1.append(L)
    print(L1)

def main():
    L1 = []
    n = int(input("input size of list: \n"))
    for i in range(n):
        x = int(input("Input a number: "))
        L1.append(x)
    printSubsets(L1,n)


if __name__ == "__main__":
    main()
    