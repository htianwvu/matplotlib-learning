
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1: subplot2grid#####

#method 2: gridspec
##########################


#method 3: easy to define structure
##########################
f,((ax11,ax12),(ax21,ax22))= plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])

plt.tight_layout()


plt.show()


