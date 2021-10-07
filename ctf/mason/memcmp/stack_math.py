# 0x0000555555400c32 <+328>:   mov    BYTE PTR [rbp-0x60],al
# 0x0000555555400eab <+961>:   mov    BYTE PTR [rbp-0x5f],al
# 0x0000555555400f81 <+1175>:  mov    BYTE PTR [rbp-0x5e],al
# ...
# 0x00005555554026a0 <+7094>:  mov    BYTE PTR [rbp-0x48],al

# $rbp   : 0x00007fffffffdb80

rbp = 0x00007fffffffdb80
arr = 0x60

starting_address = rbp - arr
print(hex(starting_address))