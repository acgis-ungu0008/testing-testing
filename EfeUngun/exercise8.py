##Exercise 7:  Decimal Degrees to DMS
##Input: decimal degrees is 95.41805
##Output: <decimal degree> = <dd>:<mm>:<ss.sss>


dms=95.41805
x=int(95.41805)
y=int((95.41805 - 95) *60)
z=(95.41805-95 - 25.0/60)*3600
DMS= x+y+z

print "%.5f =%dd:%dm:%ds"  % (dms,x,y,z)









