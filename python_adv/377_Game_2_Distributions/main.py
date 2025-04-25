'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

# Seeding for reproducibility


# sampling from each of the six distributions

S = 1000000
# plotting histograms for each of the distributions
plt.subplot(3,2,1)
beta = np.random.beta(4, 20, size=S)*100
bins = np.arange(-5, 51, 1)
plt.hist(beta, bins, color="red" )
plt.title("Beta")

plt.subplot(3,2,2)
exp = np.random.exponential(0.1, size=S)*100
bins = np.arange(-1, 51, 1)
plt.hist(exp, bins, color="green", alpha=0.5)
plt.title("Exponential")

plt.subplot(3,2,3)
gamma = np.random.gamma(2, 0.1, size=S)*100
bins = np.arange(-1, 51, 1)
plt.hist(gamma, bins, color="black", alpha=0.8, orientation="horizontal")
plt.title("Gamma")

plt.subplot(3,2,4)
laplace = np.random.laplace(0, 0.5, size=S)*100
bins = np.arange(-1, 51, 1)
plt.hist(laplace, bins, color="orange")
plt.title("Laplace")

plt.subplot(3,2,5)
normal = np.random.normal(0, 3, size=S)
bins = np.arange(-10, 12, 1)
plt.hist(normal, bins)
plt.title("Normal")

plt.subplot(3,2,6)
poisson = np.random.poisson(lam=3, size=S)
bins = np.arange(-1, 12, 1)
plt.hist(poisson, bins)
plt.title("Poisson")


# adjust the sub-plots to fit the titles and labels
plt.tight_layout()
# save the plot as plot.png
plt.savefig('plot.png')