import numpy as np

ar = 2 * np.arange(6)
print ar
print ar[1:5:2]
print ar[1:6:2] # range # ^^^ to include last element (endIndex)

# first n elements
print ar[:4]   #startIndex = 0 step =1

# element 4 until end
print ar[4:]

# slice with stepValue= 3
print ar[::3]
print ar[::2]

ar2 = np.array([
    [0, 1, 2, 3, 4, 5],
[10, 11, 12, 13, 14, 15],
[20, 21, 22, 23, 24, 25],
[30, 31, 32, 33, 34, 35],
[40, 41, 42, 43, 44, 45],
[50, 51, 52, 53, 54, 55]
])

print ar2

print 'slice 1:\n', ar2[0, 3:5]
print 'slice 2:\n', ar2[4:, 4:]
print 'slice 3:\n', ar2[2::2, ::2] # 2::2 -> start row 2 step 2 / ::2 -> columns in step 2