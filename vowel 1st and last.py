a=input()
l1=[]
b=a.split(' ')
l2=['a','e','i','o','u']
for i in b:
    c=i[-1]
    if c in l2:
        m=b.index(i)
        m+=1
        d=b[m][0]
        if d in l2:
            l1.append("True")
            
        else:
            l1.append("False")
if "True" in l1:
    print("True")
else:
    print("False")

