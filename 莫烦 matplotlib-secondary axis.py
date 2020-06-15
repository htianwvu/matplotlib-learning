
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 = -1*y1

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x,y1,'b-')
ax2.plot(x,y2,'r')

ax1.set_xlabel('X data')
ax1.set_ylabel('y1',size= 20,color='b')
ax2.set_ylabel('y2',size= 20,color='r')

plt.show()


