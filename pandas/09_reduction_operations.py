import numpy as np

ar = np.arange(1,5)
print ar.prod()



ar1 = np.array([np.arange(1,6), np.arange(1,6)])
print ar1


print 'ar1 axis 0:', np.prod(ar1, axis=0)
print 'ar1 axis 1:', np.prod(ar1, axis=1)


ar2 = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print 'ar2:\n', ar2
print 'ar2 mean:\n', ar2.mean()
print 'ar2 median:\n', np.median(ar2)
print 'ar2 std:\n', ar2.std()

print 'ar2 cumsum:\n', ar2.cumsum()


