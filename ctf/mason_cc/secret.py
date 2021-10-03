#!/usr/bin/env python3

def valid_password(password):
    password = list(password)
    if(len(password) != 31):
        return False
    for x in range(0, len(password)):
        val = ord(password[x])
        val = val + 5
        password[x] = chr(val)
    if(password[:8] != ['r', 'f', 'x', 't', 's', 'h', 'h', '\x80']): # fail if 0:8 DOES NOT match the given list
        return False
    if(password[-1] != '\x82'): # fail if last value is NOT EQUAL to '\x82'
        return False
    password = password[8:-1]
    for x in range(0, len(password)):
        val = ord(password[x])
        val = val - 10
        password[x] = chr(val)
    password = password[::-1]
    password = "".join(password) # Convert to string
    if(password != 'deA?%@JDQE%#AIJDE\x1e%#<E'):
        return False
    return True

print("Please enter the password")
password = input().strip()
if(valid_password(password)):
    print("Hooray!!!")
else:
    print("Bad password :(")
