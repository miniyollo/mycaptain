l=[]

for i in range(4):
    ele=int(input("enter elements of list"))
    l.append(ele)
    i=i+1

for ele in l:
    if ele>=0:
        print(ele)
    ele=ele+1
