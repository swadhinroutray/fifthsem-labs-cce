def main():
  f = open("input.txt","r+")
  readStream = f.readlines()
  L=[]
  L1=[]
  for line in readStream:
      L.append(line)
  print("Lines")
  print(len(L))
 
  f.close()
 
  f = open("input.txt","r+")
  readChars = f.read()
  print(readChars)
  for char in readChars:
      L1.append(char) 
  print(L1)
  print("Words = ")
  print(len(L1))
  wordcount=0
  for line in L:
      wordcount+=len(line.split())
  print("WordCount  = ", wordcount)
if __name__ == "__main__":
    main()
