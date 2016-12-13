import numpy as np



ar = np.arange(15)
print ar

ar2 = np.arange(0, -10, -1)[::-1]
print ar2

ar[:10]=ar2

print ar