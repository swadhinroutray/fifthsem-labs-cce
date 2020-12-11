def main():
    f = open("input.txt","r+")
    readStream = f.read()
    L1 = readStream.split(" ")
    print(L1)
    word={}
    word[L1[0]] =1
    for i in range(1,len(L1),1):
        if L1[i] in word:
            word[L1[i]] +=1
        else:
            word[L1[i]] =1
    print(word)
if __name__ == "__main__":
    main()
