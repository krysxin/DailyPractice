import numpy as np
from scipy import stats


numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(stats.mode(numbers)[0][0])
# print(int(stats.mode(numbers)[0]))