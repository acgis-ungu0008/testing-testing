##Exercise 6: Number of bears
##Input: Bear density in bears/sq.km is 4
##Input: Area of a selected polygon in sq.meters is 10000000
##Output: When bear density is <bear per sq km> bears/sq.km and area is <sq.m> sq.m.\n the probable number of bears is <z>

bears_density=4
selected_Area_sqm= 10000
bear_In_the_selected_area=bears_density*selected_Area_sqm

if (bears_density==4 and selected_Area_sqm==10000):
    print "probable number of bear is = %d bears" % (bear_In_the_selected_area)