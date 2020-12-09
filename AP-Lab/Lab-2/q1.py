
x = {}

sentence  = input("Input a sentence \n")

sentence =sentence.split()
print(sentence)
key =0
for i in range(len(sentence)):
    x[key] = i
    key=key+1
print(len(x))