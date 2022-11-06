f = open("testing.txt", "w")
f.write("hello welcome to the testing file")
f.close()

f = open("testing.txt", "r")
for x in f:
    print(x)