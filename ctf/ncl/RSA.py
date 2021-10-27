n = 1079
e = 43
c = [996, 894, 379, 631, 894, 82, 379, 852, 631, 677, 677, 194, 893]

p = 13
q = 83
lamb = 492

d = pow(43, -1, 492)

secret = ""

for num in c:
    secret +=  str((num ** d) % n) + " "
print(secret)