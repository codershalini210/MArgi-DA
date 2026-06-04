import numpy as np 

ary = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
ary1 = np.array([101,2,3,42])
print(ary)
print(ary1)
print(ary.ndim)
print(ary1.ndim)
print("shape of ary is ", ary.shape)
print("shape of ary1 is ", ary1.shape)
print("datatype of ary is ",ary.dtype)

zeroary = np.zeros((2,2))
print(zeroary)

oneary = np.ones((2,2))
print(oneary)
oneary = oneary+5
print(oneary)


aryrange = np.arange(10,15)
print(aryrange)


aryrange2 =np.array([ np.arange(10,15),
                      np.arange(110,115),
                        np.arange(210,215) ])
print(aryrange2)

