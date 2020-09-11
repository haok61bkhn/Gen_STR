f=open("alphabet.txt").read().split("\n")
s=""
for x in f:
    s+=x.split(",")[-1]
print(s)