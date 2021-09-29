x = "1101101 10121 1303 421 302 201 143 146 116 47 96 86 6d 79 79 5a 62 2b 5a 51 28 5a"
li = x.split(" ")
print(li)

out = ""
for i in range(len(li)):
    out += str(int(li[i], i+2)) + " "
print(out)