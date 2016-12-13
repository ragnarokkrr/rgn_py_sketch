import numpy as np


ar = np.array([2, -1, 6, 3], dtype='float')

print ar, "dtype:", ar.dtype


ar2 = np.array([2, 4, 6, 8])
print ar2, "dtype:", ar2.dtype


sar = np.array(['Goodbye', 'Welcome', 'Tata', 'Goodnight'])

print sar, sar.dtype # S9 -> stirng + lenght of longest string\


bar = np.array([True, False, True])
print bar, bar.dtype



#type conversion


f_ar = np.array([3, -2, 8.18])
print f_ar, f_ar.dtype

i_ar = f_ar.astype(int)
print i_ar, i_ar.dtype
