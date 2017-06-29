import matplotlib.pyplot as plt

plt.plot([1,2,3,4])

plt.show()

x = range(0, 100)
y = [v*v for v in x]

plt.plot(x, y, 'r-')

# line style
# color : bgrcmykw
# marker : ov^s+.