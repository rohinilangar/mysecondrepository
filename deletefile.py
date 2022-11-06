f = open("testng.txt", "w")
f.write("hello welcome tho the testing file")
f.close()


import os
os.remove("testing.txt")

f = open("testing.txt", "r")
print(f.read(5))