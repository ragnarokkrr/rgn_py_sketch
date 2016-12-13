import numpy as np



ar1 = np.arange(12)
print ar1


ar2 = ar1[::2]
print ar2

ar2[1] = -1
print ar2


#copy


ar3 = np.arange(8)
print ar3

ar3_cp = ar3[:3].copy()
ar3_cp[0] = -1
print ar3_cp