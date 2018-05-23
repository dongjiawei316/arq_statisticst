# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
len = 8;
step = 0.4;

def build_staticslayer(z_value):
    x = np.arange(0, 0.5, 0.01);
    y = np.arange(1, 250, 5);

    y1 = np.divide(1000, y)
    x, y1 = np.meshgrid(x, y1)

    z = np.exp(x *( (2*x - x ** 2)**y1))

  #  x1 = np.multiply(2, x)
  #  x2 = np.power(x, 2)
  #  x3 = np.subtract(x1, x2)
# x4 = np.power(x3, y1)
 #   z1 = np.multiply(x4, x)
  #  z2, z3 = np.meshgrid(z1, x)
  #  z = z2 + z3;

    print(z)

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

#x5, y5, z5 = build_layer(0.15);
#ax.plot_surface(x5, y5, z5, rstride=1, cstride=1, color='pink')

# x2, y2, z2 = build_layer(-0.26);
# ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, color='yellow')
#
# x6, y6, z6 = build_layer(-0.22);
# ax.plot_surface(x6, y6, z6, rstride=1, cstride=1, color='pink')

# x4, y4, z4 = build_layer(0);
# ax.plot_surface(x4, y4, z4, rstride=1, cstride=1, color='purple')

#x3, y3, z3 = build_gaussian_layer(0, 1)
#ax.plot_surface(x3, y3, z3, rstride=1, cstride=1, cmap='rainbow')
plt.show()