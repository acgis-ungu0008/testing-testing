##Exercise 7:  DMS to demical degress
##Input:  Degrees is 95
##Input:  Minutes is 25
##Input:  Second is 5
##Output: Output: <deg>:<min>:<sec>=dd.ddddd

d=95
m=25.0
s=5.0
dec_deg= d+(m/60)+(s/3600)

print "%dd:%dm:%ds = %.4f" % (d,m,s,dec_deg)









