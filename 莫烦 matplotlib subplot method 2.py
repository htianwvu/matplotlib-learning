
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1: subplot2grid
##########################
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')


ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,)
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0))
ax5 = plt.subplot2grid((3,3),(2,1))





#method 2: gridspec
##########################
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])


#method 3: easy to define structure
##########################


plt.tight_layout()








plt.show()


