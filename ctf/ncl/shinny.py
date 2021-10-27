from types import CodeType

ENC = [171, 179, 161, 213, 185, 187, 172, 174, 213, 202, 205, 193, 203]

def check(inp):
    inputString = list(map(lambda x: ord(x), inp))
    payload = bytes.fromhex('67005a00650144005d165a026502640041005a036500a0046503a101010071086500610564015300')
    print(payload)
    code = CodeType(0, 0, 0, 0, 4, 64, payload, (248, None),  ('ret', 'inputString', 'i', 'step', 'append', 'returnVal'), (), '<source>', '<module>', 2, b'\x04\x01\x08\x01\x08\x01\x0c\x01')
    # stacksize = 4, flags = 64, codestring = payload, constants = (248, None), names = ('ret', 'inputString', 'i', 'step', 'append', 'returnVal'), varnames = (), filename = '<source>', name = '<module>', firstlineno = 2, lnotab = b'\x04\x01\x08\x01\x08\x01\x0c\x01'
    exec(code)
    if returnVal == ENC:
        print('Congrats you have solved my puzzle')
    else:
        print('Eck')

def main():
    inp = input()
    check(inp)

if __name__ == '__main__':
    main()