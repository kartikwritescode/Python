import statistics as stats
import numpy as np

data = [10, 20, 20, 40, 50, 60, 70, 80, 90, 90, 90]

mean_value = stats.mean(data)
median_value = stats.median(data)

try:
    mode_value = stats.mode(data)
except stats.StatisticsError:
    mode_value = "No unique mode found"

std_dev = stats.stdev(data)

print("Given Data:", data)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Standard Deviation (SD):", std_dev)
print(stats.__dir__())


num1 = [10,12,54,78,58,33,24,54,32,63]
n = len(num1)

print("\nData to find mean, median, mode & standard deviation : ", num1)


getsum = sum(num1)
mean = getsum / n
print("Mean = " + str(mean))


num1.sort()
if n % 2 == 0:
    median1 = num1[n//2]
    median2 = num1[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = num1[n//2]
    print("Median = " + str(median))

from collections import Counter
data = Counter(num1)
getmode = dict(data)
mode = [k for k, v in getmode.items() if v == max(list(data.values()))]
if len(mode) == n:
    getmode = "No mode found"
else:
    getmode = "Mode = " + ', '.join(map(str, mode))
    print(getmode)

print("Standard Deviation = ",np.std(num1))