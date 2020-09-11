from alphabets import *
# print('aa' in alphabet)
def check(x):
    for y in x:
        if(y not in alphabet[:-1]):
            print(y)
            return False
    return True

new_string=[]

strings1 = open("str/str.txt").read().split("\n")
for x in strings1:
    if(check(x)):
        new_string.append(x.lower())
    

    
strings2=open("str/dictionary.txt").read().split("\n")
for x in strings2:
    for y in x.split(" "):
        if(check(y)):
            new_string.append(y.lower())

strings3=open("str/dic_clean.txt").read().split("\n")
for x in strings2:
        if(check(x)):
            new_string.append(x.lower())
new_string=set(new_string)

f=open("str/clean.txt","w+")
for x in new_string:
    f.write(x+"\n")


