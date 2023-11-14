boyname=input("enter your boy name:").upper()
girlname=input("enter your partner name:").upper()
for x in boyname:
    for x in girlname:
        boyname=boyname.replace(x,"")
        girlname=girlname.replace(x,"")
name=boyname+girlname
l=len(name)
r=l%6
if r==0:
    print("Relationship status:Friends")
elif r==1:
    print("Relationship status:lovers")
elif r==2:
    print("Relationship status:affection")
elif r==3:
    print("Relationship status:marriage")
elif r==4:
    print("Relationship status:enemy")
elif r==5:
    print("Relationship status:siblings")
else:
    pass