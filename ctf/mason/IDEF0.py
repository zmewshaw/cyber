from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

I1 = "942a502bd5ff741f21c734a824ada7772412ee5cfb3ef345"
I2 = "3a424c529b626e3"
I3 = "4162c9243a645e2"

# translated vars
ct = bytes.fromhex(I1)
key = bytes.fromhex(I2)
iv = bytes.fromhex(I3)

print(key)
print(iv)
print(ct)
def blowfish_decrypt(key, iv, ct):
    cipher = Cipher(algorithms.Blowfish(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    print((decryptor.update(ct) + decryptor.finalize()).hex())

blowfish_decrypt(key, iv, ct)

# TURNS OUT YOU CAN JUST PUT IT INTO CYBERCHEF