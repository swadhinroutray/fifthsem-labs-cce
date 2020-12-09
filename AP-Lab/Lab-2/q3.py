import random
import re


def checkSpecial(s):
     if not re.match(r'^[_\W]+$', s):
        return
     else:
        print('Contains only Special Characters: ' + s +'\n')


n = int(input("input size of dictionary"))

dic ={}
nums =0
suma=0
strcat=''
for i in range(n):
    x = int(input("Input 1 for integer and 2 for string\n"))
    if x==1 :
        num = int(input("enter a number \n"))
        suma =suma+num
        nums =nums+1
        dic[random.randrange(0,100)] = num
    else:
        string = input("Enter string \n")
        dic[random.randrange(0,100)] = string
        strcat= strcat +string
        checkSpecial(string)
if nums!=0:
    print("Average: ")
    print(float(suma/nums))

print("\nConcatenated String: " + strcat)
search = input("\nInput string to be searched")
key_list = list(dic.keys())
val_list = list(dic.values())
if search in val_list:
    print(key_list[val_list.index(search)])
else:
    print(search+" does not exist in dictionary")
print(dic)