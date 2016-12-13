import numpy as np

ar1 = np.array([0,1,2,3])
ar2 = np.array([[0,3,5], [2,8,7]])

print ar1

print ar2


ar3 = np.arange(12)


print ar3


#linear evenly spaced elements
ar5 = np.linspace(0, 2.0/3, 4)

print ar5


ar7 = np.ones((2, 3, 2))

print ar7

ar8 = np.zeros((4, 2))


print ar8

# identity matrix\
ar9 = np.eye(3)
print ar9


# diagonal array
ar10 = np.diag((2,1,4,6))
print ar10



#rand

np.random.seed(100) # set seed
ar11 = np.random.rand(3)
print ar11



ar13 = np.empty((3,2))
print ar13




