#NOT MY WORK

C = 16381842941209689065049461047973294179844309716670688013050623837652137334284143868292549783491379708584891716069631961577173146456158094873265647348702115027900326461908294166034591559237123978352237779584917709964512742991247999719562046418853578481274454679355567176288308362340380242868583227610205015867

p = 53393669192444171557534559682731025693603623615925594984688200261759729962508305791959488848744352454925546143126400310621662840790967520750705876631955671020478647

q = 3118406977450779134834147548390858451644711064141377558991877129510255898654713730079801618931687123899025065634150187751262562515462361357350587

dp = 6639888977500038118832211749305855614429551741303288205520680411574252699916729362107967012790736111015810932244078345538650718715326995347944716641751052364571173

dq = 531875935638567666649008976546271812449220749728738244875584823132972831151294537052840723506086617802818288656156534456621647676851828360353157


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def int2Text(number, size):
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")


qinv = modinv(q, p)

m1 = pow(C, dp, p)  # (C ** dp) % p
m2 = pow(C, dp, p)  # (C ** dq) % q

h = ((m1 - m2) * qinv) % p
y = m2 + (q * h)

print(str(int2Text(y, 100)))