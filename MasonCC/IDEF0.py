raw_IV = "942a502bd5ff741f21c734a824ada7772412ee5cfb3ef345"
raw_C0 = "3a424c529b626e3"
raw_C1 = "4162c9243a645e2"
IV = []
C0 = []
C1 = []
for i in range(len(raw_IV)):
    IV.append(bin(ord(raw_IV[i])))
for i in range(len(raw_C0)):
    C0.append(bin(ord(raw_C0[i])))
    C1.append(bin(ord(raw_C1[i])))
