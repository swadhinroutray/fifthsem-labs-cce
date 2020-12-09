
def multiply(L,n):
    val =1
    for i in range(n):
        val = val* L[i]

    return val 



def main():
    L1 = []
    n = int(input("input size of list: \n"))
    for i in range(n):
        x = int(input("Input a number: "))
        L1.append(x)
    multval = multiply(L1,n)
    print("Value on multiplication = ")
    print(multval, end ="\n")


if __name__ == "__main__":
    main()
