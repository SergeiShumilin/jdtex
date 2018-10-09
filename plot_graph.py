import matplotlib.pyplot as plt
import numpy as np



def plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    w = np.arange(2,17)
    p = np.arange(0,1,0.01)
    for w in w:
        if w==2:
            ax1.plot(p, func1(p, w),linewidth=3)
            ax2.plot(p, func2(p, w),linewidth=3)
        else:
            ax1.plot(p,func1(p,w))#rrrrrrrrrrrrr
            ax2.plot(p,func2(p,w))
    plt.show()

def testpyplt(w):
    p = np.arange(0,1,0.2)
    plt.plot(p,1 - (1 - p)**w - p*w)
    plt.show()

def func1(p,w):
    return 1 - (1 - p)**w - p*w

def func2(p,w):
    return 1 - p**w - (1-p)*w


if __name__=='__main__':
    testpyplt(3)