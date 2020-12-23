import string
def main():
    f = open("lines.txt","r+")
    stream = f.read().splitlines()
    print(stream)
    L=[]
    for i in stream:
        L.append(i[::-1])
    print(L)
    f1 = open("reverselines.txt",'a')
    for i in L:
        f1.writelines(i +'\n')
if __name__ == "__main__":
    main()