import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

'''
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
'''

# sample 1
'''
x = range(0, 100)
y = [v*v for v in x]

ax1.plot(x, y)
ax2.bar(x, y)
plt.show()
'''

# sample 2
x = np.arange(0.0, 2*np.pi, 0.1)
sin_y = np.sin(x)
cos_y = np.cos(x)

# axes 1
ax1.plot(x, sin_y, 'b--')
ax1.set_xlabel('X')
ax1.set_ylabel('sin(x)')

ax2.plot(x, cos_y, 'r--')
ax2.set_xlabel('X')
ax2.set_ylabel('cos(x)')

plt.show()


