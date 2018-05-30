# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(8,8), dpi=400)
ax = Axes3D(fig)
len = 8;
step = 0.4;

def build_staticslayer(z_value):
    x = np.arange(0, 50, 1);
    y = np.arange(1, 250, 5);

    y1 = np.divide(1000, y)
    y2 = np.rint(y1)

    x1 = x / 100


    x, y = np.meshgrid(x, y)
    z = (x1 *( (2*x1 - x1 * x1)**(1000/y)))*100

    #print(y2)
    #print(z)
    return (x, y, z);

def build_layer(z_value):
    x = np.arange(-len, len, step);
    y = np.arange(-len, len, step);
    z1 = np.full(x.size, z_value/2)
    z2 = np.full(x.size, z_value/2)
    z1, z2 = np.meshgrid(z1, z2)
    z = z1 + z2;

    x, y = np.meshgrid(x, y)
    return (x, y, z);

def build_gaussian_layer(mean, standard_deviation):
    x = np.arange(-len, len, step);
    y = np.arange(-len, len, step);
    x, y = np.meshgrid(x, y);
    z = np.exp(-((y-mean)**2 + (x - mean)**2)/(2*(standard_deviation**2)))
    z = z/(np.sqrt(2*np.pi)*standard_deviation);
    return (x, y, z);

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
x1, y1, z1 = build_staticslayer(0.2);
ax.plot_surface(x1, y1, z1, rstride=1, cstride=1, color='green')

ax.autoscale_view()
my_z_ticks = np.arange(0, 14, 0.5)
ax.set_zticks(my_z_ticks)
ax.set_xlabel("original loss rate (%) ")
ax.set_ylabel('looptime (ms)')
ax.set_zlabel("final loss rate (%s)")

#plt.show()
plt.savefig('loss_rate_3D.png', bbox_inches = 'tight')