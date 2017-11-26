a = "011"
b = "0"
c = "0"

ad1 = "101"
bd1 = "1"
cd1 = "0"

ad2 = "100"
bd2 = "1"
cd2 = "0"

d = int(a,2) + int(b,2) + int(c,2) +6
dd1 = int(ad1,2) + int(bd1,2) + int(cd1,2)
dd2 = int(ad2,2) + int(bd2,2) + int(cd2,2)

print d
print dd1
print dd2
print "%d,%d%d" %(d,dd1,dd2)