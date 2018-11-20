import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
point_test = np.array([1,-1,1])
normal_test = np.array([1,-2,1])
sum(point_test*normal_test)
point1 = np.array([0,0,0])
normal1 = np.array([1,-2,1])

point2 = np.array([0,-4,0])
normal2 = np.array([0,2,-8])

point3 = np.array([0,0,1])
normal3 = np.array([-5,4,9])
d1 = -np.sum(point1*normal1)
d2 = -np.sum(point2*normal2)
d3 = -np.sum(point3*normal3)
d1,d2,d3

xx , yy = np.meshgrid(range(5),range(5))
xx
z1 = (-normal1[0]*xx - normal1[1]*yy -d1)*1./normal1[2]
z2 = (-normal2[0]*xx - normal2[1]*yy -d2)*1./normal2[2]
z3 = (-normal3[0]*xx - normal3[1]*yy -d3)*1./normal3[2]

%matplotlib inline
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color="red")
plt3d.plot_surface(xx,yy,z2,color="green")
plt3d.plot_surface(xx,yy,z3,color="blue")
#3 boyutlu spiral cizim
fig = plt.figure()
ax = fig.add_subplot(111,projection'3d')
n = 1000
theta_max = 0 * np.pi
theta =np.linspace(0,theta_max,n)
x = np.sin(theta)
y = np.cos(theta)
z = theta
ax.plot(x , y ,z ,'b' ,lw=2)
#iki boyutlu spiral cizimi
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from math import exp,sin,cos
from pylab import *
mpl.rcParams['legend.fontsize'] = 10
resim = plt.figure()
ax = resim.gca(projection='3d')
n=100
a=10
b=0.05
hesapla=np.linspace(0, 500, 10000)
x_1=a*exp(b*hesapla)*cos(hesapla)
y_1=a*exp(b*hesapla)*sin(hesapla)
ax.plot(x_1, y_1)
ax.legend()

plt.show()
