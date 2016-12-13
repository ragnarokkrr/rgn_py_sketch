import numpy as np

np.random.seed(10)
ar = np.random.random_integers(0, 24, 10)
print ar

even_mask = (ar % 2==0)
print even_mask


ar2 = np.array(['Hungary', 'Nigery', 'Guatemala', '', 'Poland', '', 'Japan'])
print ar2, ar2.dtype

ar2[ar2==''] = 'USA'
print ar2



ar3 = 11 * np.arange(0,10)
print ar3

print ar3[[1,3,4, 2, 7]] # array of indeces produces another array

