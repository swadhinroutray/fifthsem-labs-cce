def checkPwd(pwd):
    countUpper =0
    countLower=0
    countDigit=0
    # print(l)
    for i in pwd:
        if i>='A' and i<='Z':
            countUpper+=1
        elif i>='a' and i<='z':
            countLower+=1
        elif i>='0' and i<='9':
            countDigit+=1
    print(countUpper,countLower,countDigit)
    if countUpper >=2 and countLower>=1 and countDigit>=2:
        return True
    return False
def main():
    L1=[]
    L2=[]
    dict ={}
    for i in range(3):
        x = input("Input name: ")
        y = input("Input Password: ")
        L1.append(x)
        L2.append(y)
        check = checkPwd(y)
        if check == True:
            dict[x] = y
    print(dict)
    asc = list(dict.keys())
    print(asc)
    asc.sort()
    


if __name__ == "__main__":
    main()