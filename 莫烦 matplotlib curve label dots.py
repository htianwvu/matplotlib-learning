
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,50)
y = 2*x + 1

plt.figure(num=1)
plt.plot(x,y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


x0 =1
y0 =2*x0 +1
plt.scatter(x0,y0)









plt.show()


