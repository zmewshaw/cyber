x = ['d', 'e', 'A', '?', '%', '@', 'J', 'D', 'Q', 'E', '%', '#', 'A', 'I', 'J', 'D', 'E', '\x1e', '%', '#', '<', 'E']
x = x[::-1] # <- LINE 20
for i in range(len(x)):
    val = ord(x[i])
    val = val + 10
    x[i] = chr(val)
print("Indexes after 7: " + str(x))
x = ['r', 'f', 'x', 't', 's', 'h', 'h', '\x80'] + x + ['\x82']
print("precheck: " + str(x))
for i in range(len(x)):
    val = ord(x[i])
    val = val - 5
    x[i] = chr(val)
print("final: " + str(x))
print("".join(x))

# <-------------------------------------->

# password = []
# for i in range(len(x)):
#     password.append(str(chr(i + 97)))
# print(password)
# for x in range(0, len(password)):
#     val = ord(password[x])
#     val = val - 10
#     password[x] = chr(val)
# print(password)
# for x in range(0, len(password)):
#     val = ord(password[x])
#     val = val + 10
#     password[x] = chr(val)
# print(password)