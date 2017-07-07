import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 5, 11)
print (x)

y = x ** 2
print (y)

# ========================================
# Functional Method...
# ========================================

plt.plot(x, y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# multi plot 그리기
plt.subplot(1,2,1)
plt.plot(x,y, 'r-')

plt.subplot(1,2,2)
plt.plot(y, x, 'b-')


# ========================================
# Object Oriented Method...
# ========================================

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Set Title')



fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes1.set_title('Larger Plot')
axes2.plot(y, x)
axes2.set_title('Smaller Plot')

# ========================================
# Object Oriented Method...
# ========================================

fig,axes = plt.subplots(nrows=1, ncols=2)

for current_ax in axes:
    current_ax.plot(x, y)


fig,axes = plt.subplots(nrows=1, ncols=3)
axes[0].plot(x,y)
axes[1].plot(x,y)
axes[2].plot(x,y)


