import numpy as np

if __name__ == '__main__':
    a = np.arange(10)
    print(a)
    print(a.shape)
    print(a.ndim)

    print('-------------')
    b = np.arange(10).reshape(2,5)
    print(b)
    print(b.shape)
    print(b.ndim)

    c = np.arange(24).reshape(2,3,4)
    print(c)
    print(c.shape)
    print(c.ndim)
