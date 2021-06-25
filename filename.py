file=input("Enter File name:")
print("file name is :",file)

ext=file.split('.')

ex=ext[1]
print("your extension is:",ex)

if(ex=='py') :
    print("file type is PYTHON!")
elif(ex=='c') :
    print("file type is C!")
elif(ex=='cpp') :
    print("file type is C++!")
else:
    (":)")
