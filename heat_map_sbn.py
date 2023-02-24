import pandas as pd

import numpy as np
import seaborn as sns

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Seaborn example: DataFrame, like a matrix
glue = sns.load_dataset("glue").pivot("Model", "Task", "Score")

# Ex. Python Tutorial
np.random.seed(0)
sns.set()
uniform_data = np.random.rand(10, 12)

# Replicating Matt's ex
# 1: time series: pv distance
# 2: time series: ego speed

# ego_spd = 70 * np.random.rand(1000, 1)
ego_spd = 100 * [70] + 800 * [65] + 100 * [60]
pv_dist = np.random.rand(1000, 1)
pv_dist2 = [i[0] for i in pv_dist]
pv_dist3 = [100 * i for i in pv_dist2]

n = 10

spd_bins = list(np.linspace(35, 80, n))
spd_binned = np.digitize(spd_bins, ego_spd, right=True)

dist_bins = list(np.linspace(1, 100, n))
dist_binned = dict()
for i, dist_bin_low in enumerate(dist_bins):
    if i < len(dist_bins):
        dist_bin_high = dist_bins[i+1]
    else:
        dist_bin_high = dist_bins[-1]
    bin_step = 1.111111111111
    this_bin = list()
    for dist in pv_dist3:  # for each sample point
        if dist_bin_low <= dist < dist_bin_high:
            this_bin.append(dist)
    dist_binned[i] = this_bin

print(dist_binned)

# Input like Matt's
df_2cols = pd.DataFrame({'ego_spd': ego_spd, 'pv_dist': pv_dist3})

# Output template
df_2d = pd.DataFrame(index=spd_bins, columns=dist_bins)

# Loop through output


billy = 1
