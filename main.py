import numpy as np
import matplotlib.pyplot as plt

# Set sample size
size = 1000

# 1. Normal Distribution (mean=0, std=1)
normal_data = np.random.normal(loc=0, scale=1, size=size)

# 2. Uniform Distribution (range 0 to 1)
uniform_data = np.random.uniform(low=0, high=1, size=size)

# 3. Exponential Distribution (scale = 1/lambda)
exponential_data = np.random.exponential(scale=1, size=size)

# 4. Binomial Distribution (n=10 trials, p=0.5)
binomial_data = np.random.binomial(n=10, p=0.5, size=size)

# 5. Poisson Distribution (lambda = 3)
poisson_data = np.random.poisson(lam=3, size=size)

# Plot all distributions
plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.hist(normal_data, bins=30)
plt.title("Normal Distribution")

plt.subplot(2,3,2)
plt.hist(uniform_data, bins=30)
plt.title("Uniform Distribution")

plt.subplot(2,3,3)
plt.hist(exponential_data, bins=30)
plt.title("Exponential Distribution")

plt.subplot(2,3,4)
plt.hist(binomial_data, bins=15)
plt.title("Binomial Distribution")

plt.subplot(2,3,5)
plt.hist(poisson_data, bins=15)
plt.title("Poisson Distribution")

plt.tight_layout()
plt.show()