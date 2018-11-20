import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline
%matplotlib notebook

#teget olan vektorun buyuklugu baslangıc nokrası fonksıyonun gercek degerlerı
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#a b degerler direk 3 ve 2 olarak verilmiştir


theta_max = 8*np.pi
theta = np.linspace(0,theta_max,n)
z = theta
x = 3*np.cos(theta)
y = 2*np.sin(theta)
ax.plot(x,y,z,'b',lw=2)

theta_current = 3 *np.pi/2
x_1=3*np.cos(theta_current)
y_1=-2*np.sin(theta_current)
z_1=1

x_2=3*np.sin(theta_current)
y_2=2*(-np.cos(theta_current))
z_2=theta_current

x_3 = x_1 + x_2
y_3 = y_1 + y_2
z_3 = z_1 + z_2
x_s=[x_3,x_2]
y_s=[y_3,y_2]
z_s=[z_3,z_2]

ax.plot(x_s,y_s,z_s)
plt.show()
