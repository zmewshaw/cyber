from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
import random


key = bytes.fromhex(os.environ.get('CTFKEY'))
iv  = bytes.fromhex(os.environ.get('CTFIV'))





print("Welcome to the decrypt service!")
print("Enter your iv/ciphertext pair to decrypt:")
ct_iv=input()
iv=bytes.fromhex(ct_iv[:32])
ct=bytes.fromhex(ct_iv[32:])
cipher=AES.new(key, AES.MODE_CBC, iv)

out=cipher.decrypt(ct)
try:
        unpad(out,16)
except:
        print("An error has occured in unpad()")
        exit(0)
print("Your input has been stored. Thank you for not being a robot.")
