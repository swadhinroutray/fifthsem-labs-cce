def main():
  f = open("reverse.txt","r+")
  readStream = f.readlines()
  L1=[]
  for line in readStream:
      L1.insert(0,line)
  f1 = open("afterreverse.txt","w")
  for line in L1:
    f1.write(line)
if __name__ == "__main__":
    main()
