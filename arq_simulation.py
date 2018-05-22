# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

original_loss_rate = list(range(1, 50))
x_v = [x * 0.01 for x in original_loss_rate]

n = 3
loss_rate = [x * (2*x - x ** 2)**n  for x in x_v]

plt.scatter(original_loss_rate, loss_rate, s =10)

n = 5
loss_rate = [x * (2*x - x ** 2)**n  for x in x_v]
plt.scatter(original_loss_rate, loss_rate, s =10)

n = 10
loss_rate = [x * (2*x - x ** 2)**n  for x in x_v]

plt.scatter(original_loss_rate, loss_rate, s =10)
#plt.show()
plt.savefig('loss_rate.png', bbox_inches = 'tight')