
# string manipulation [start:stop:step]
# 
name = "Bro Code"

first_name = name[:3]
last_name = name[4:]
funky_name = name[::2]
#funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website = "http://google.com"
website2 = "http://axsy.com"

addr = slice(7,-4)

print(website[addr])
print(website2[addr])