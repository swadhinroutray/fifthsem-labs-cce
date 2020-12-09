import math
import cmath

def main():
       
    n = complex(input("Input a complex number: \n"))
    Sval = cmath.sin(n)
    Root = cmath.sqrt(n)
    LogVal =cmath.log(n)
    print("Sine, Root and Log values are: \n")    
    print(Sval, end ="\n")    
    print(Root, end ="\n")    
    print(LogVal, end ="\n")

if __name__ == "__main__":
    main()
