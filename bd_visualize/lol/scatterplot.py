from pylab import *

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

axes([0.025,0.025,0.95,0.95])
scatter(X,Y, s=75, c=T, alpha=0.5)

xlim(-10.5,10.5)
ylim(-1.5,1.5), yticks([])
# savefig('../figures/scatter_ex.png',dpi=48)
show()