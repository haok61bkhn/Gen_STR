import random
import string
#gen number

strings=[]
stringad=["Tổ","Khu phố","Số","số","Ấp","ấp","Thôn","thôn","Xóm","xóm","Khối","TDP","K","KP","T/phố","Q.","P.","P/","TP/","P,","Ngõ"]
sstr=[".",","]
def rannum():
    x=random.randint(1,4)
    if(x==1):
        s=str(random.randint(0,1000))
    elif(x==2):
        s=str(random.randint(0,1000))+random.choice(string.ascii_letters)
    elif(x==3):
        s=str(random.randint(0,1000))+"/"+ str(random.randint(0,1000))
    else:
        s=str(random.randint(0,1000))+"/"+ str(random.randint(0,1000))+random.choice(string.ascii_letters)
    return s
def rand():
    return random.randint(0,100)>85
for i in range(0,10):
    strings.append("0"+str(i))

for i in range(0,10000):
    strings.append(str(i))

strings1=open("str/clean.txt").read().split("\n")[1:-1]
for x in strings1:
    strings.append(x)
    if(len(x)>1):
        strings.append(x[0].upper()+x[1:])
    strings.append(x.upper())
    
strings2=open("str/address/long.txt").read().split("\n")[0:-1]
for x in strings2:
    strings.append(x)
    if(rand()):
        s=random.choice(stringad)+" "+rannum()+" "+x
        strings.append(x)


strings3=open("str/address/short.txt").read().split("\n")[0:-1]
for x in strings3:
    strings.append(x)
    if(rand()):
        s=random.choice(stringad)+" "+rannum()+" "
        strings.append(x)




strings=set(strings)

f=open("str/final.txt","w+")
for x in strings:
    f.write(x+"\n")
