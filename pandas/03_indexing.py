import numpy as np


ar = np.arange(5)
print ar, ar[0], ar[1], ar[-1], ar[-2] #cycle indexing

#reverse
ar2 = np.arange(5)
ar2_rev = ar[::-1]
print ar2, ar2_rev


#n-dim  arrays tuples of int integers
ar3 = np.array([[2, 3, 4], [9, 8, 7], [11, 12, 13]])
print ar3
print ar3[1,1]

ar3[1,1] = 5
print ar3

#retrieve row 2
print "row 2:", ar3[2]

#  retrieve colu,mn1
print 'col1:', ar3[:,1]


#index error

try:
    ar3 = np.array([0, 1, 2])
    ee = ar[5]

except IndexError as e:
    print e.message
