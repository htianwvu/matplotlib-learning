
import matplotlib.pyplot as plt
import numpy as np


n= 12
X = np.arange(n)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='r',edgecolor='white')
plt.bar(X,-Y2,facecolor='k',edgecolor='b' )
      
for x,y in zip(X,Y1):
    #ha:horizontal alighment
    plt.text(x+0.4,y+0.05,'%.2f'%y,ha='right',va='bottom')
             
for x,y in zip(X,Y2):
    #ha:horizontal alighment
    plt.text(x+0.4,-y-0.05,'-%.2f'%y,ha='right',va='top')


plt.xlim(-1,n)
plt.ylim(-1.25,1.25)

plt.xticks(())
plt.yticks(())

plt.show()


