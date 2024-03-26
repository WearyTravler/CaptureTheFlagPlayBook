from Crypto.Util.number import inverse


n = 485
e = 53
c = [153, 75, 309, 310, 74, 203, 208, 401, 310, 371, 363, 451, 125]
#c = 1537530931074203208401310371363451125
#c = 153 75 309 310 74 203 208 401 310 371 363 451 125
p = 5
q = 97

r = (p-1)*(q-1) #384

d = inverse(e,r)
#print(d)

m = []

for x in c:
   char = pow(x,d,n)
   print(hex(char)[2:-1])

#m = pow(c,d,n)
#print(hex(m))
#print(m)
