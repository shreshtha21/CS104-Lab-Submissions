'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

# Seeding for reproducibility
np.random.seed(0)
S=1000000
fig, axs=plt.subplots(3,2)


beta_samples = np.random.beta(4, 20, S) * 100
axs[0, 0].hist(beta_samples, bins=np.arange(-5, 51, 1), color='red')
axs[0, 0].set_title("Beta")

exp_samples = np.random.exponential(scale=0.1, size=S) * 100
axs[0, 1].hist(exp_samples, bins=np.arange(-1, 51, 1), color='green', alpha=0.5)
axs[0, 1].set_title("Exponential")

gamma_samples = np.random.gamma(shape=2, scale=0.1, size=S) * 100
axs[1, 0].hist(gamma_samples, bins=np.arange(-1, 51, 1), color='black', alpha=0.8, orientation='horizontal')
axs[1, 0].set_title("Gamma")

laplace_samples = np.random.laplace(loc=0, scale=0.5, size=S) * 100
axs[1, 1].hist(laplace_samples, bins=np.arange(-1, 51, 1), color='orange')
axs[1, 1].set_title("Laplace")

normal_samples = np.random.normal(loc=0, scale=3, size=S)
axs[2, 0].hist(normal_samples, bins=np.arange(-10, 12, 1))
axs[2, 0].set_title("Normal")

poisson_samples = np.random.poisson(lam=3, size=S)
axs[2, 1].hist(poisson_samples, bins=np.arange(-1, 12, 1))
axs[2, 1].set_title("Poisson")

plt.tight_layout()
plt.savefig('plot.png')