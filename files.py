import os

f = open("demofile2.txt", "a")
f.write("hello!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()


os.remove("demofile2.txt")

print("The file does not exist")