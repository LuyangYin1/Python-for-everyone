import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=42)
X = rng.integers(0, 10, (4, 6))
print(X)
# plt.style.use('seaborn-whitegrid')
plt.scatter(X[:, 0], X[:, 1], s=100)
