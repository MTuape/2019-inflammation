import numpy as np
data = np.loadtxt(
    fname = 'data/inflammation-01.csv',
    delimiter = ','
)
import matplotlib as plt
ave_inflammation =np.mean(
    data,
    axis=0
)
plt.plot(ave_inflammation)

min_inflammation =np.min(
    data,
    axis=0
)
plt.plot(min_inflammation)

