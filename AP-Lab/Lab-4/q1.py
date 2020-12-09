import math


def main():
   
    n = int(input("Input a number: \n"))
    Sval = math.sin(n)
    Root = math.sqrt(n)
    LogVal = math.log(n)
    print("Sine, Root and Log values are: \n")    
    print(Sval, end ="\n")    
    print(Root, end ="\n")    
    print(LogVal, end ="\n")
if __name__ == "__main__":
    main()
