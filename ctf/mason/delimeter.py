import sys

def create_delimited_data(data,delimiting_byte):
        out = b""
        for i in data:
                i=bytes([i])
                if i == delimiting_byte:
                        out+=delimiting_byte*2
                else:
                        out+=i
        out+=delimiting_byte
        return out.hex()

def unpack_delimited_data(data,delimiting_byte):
        out = b""
        out=data.replace(delimiting_byte*2,delimiting_byte)
        return out[:-1].hex()
inp = sys.argv[1]
delim = sys.argv[2]
data=bytes.fromhex(inp)
delim = bytes.fromhex(delim)

print(unpack_delimited_data(data,delim));