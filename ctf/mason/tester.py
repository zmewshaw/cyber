out = ""
for num in range(1000):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           out += str(num)
    #    if (str(out).__contains__("123")):
    #        break
print(out)
out.index("123")