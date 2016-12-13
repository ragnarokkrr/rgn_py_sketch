import numpy as np


ar = np.arange(0,7)*5
print ar

ar = np.arange(5) ** 4
print ar

ar = 3 + np.arange(0, 30, 3)
print ar


# element-wise operations
ar2 = np.arange(1,11)
print ar - ar2
print ar / ar2
print ar * ar2



ar3 = np.arange(1000)
print ar3


# #### array mult

ar5 = np.array([[1,1], [1,1]])
print ar5

ar6 = np.array([[2,2], [2,2]])
print ar6


print ar5.dot(ar6)

###############

# logical
print 'logical'

ar8 = np.arange(1,5)

ar9 = np.arange(5,1, -1)

print ar8 < ar9


l1 = np.array([True, False, True, False], dtype=bool)
l2 = np.array([False, False, True, False])
print np.logical_and(l1, l2)



# s log, sin, cos, and exp np.pi




ar10 = np.array([[1,2 ,3], [4, 5, 6]])
print ar10
print np.transpose(ar10)



ar11 = np.arange(0,6)
ar12 = np.array([0, 1,2 ,3, 4,5])
print np.array_equal(ar11, ar12)
