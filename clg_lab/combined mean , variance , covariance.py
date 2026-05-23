import numpy as np

def combined_mean_variance(data1, data2):
    data1, data2 = np.array(data1), np.array(data2)
    n1, n2 = len(data1), len(data2)
    mean1, mean2 = np.mean(data1), np.mean(data2)
    var1, var2 = np.var(data1, ddof=1), np.var(data2, ddof=1)
    combined_mean = (n1*mean1 + n2*mean2) / (n1 + n2)
    combined_var = (((n1 - 1)*var1 + (n2 - 1)*var2 +
                    n1*(mean1 - combined_mean)**2 +
                    n2*(mean2 - combined_mean)**2)
                    / (n1 + n2 - 1))
    return combined_mean, combined_var

def combined_covariance(X1, X2):
    n1, n2 = len(X1), len(X2)
    mean1, mean2 = np.mean(X1, axis=0), np.mean(X2, axis=0)
    cov1, cov2 = np.cov(X1, rowvar=False), np.cov(X2, rowvar=False)
    combined_mean = (n1*mean1 + n2*mean2) / (n1 + n2)
    SS_within = (n1-1)*cov1 + (n2-1)*cov2
    SS_between = (n1*np.outer(mean1 - combined_mean, mean1 - combined_mean) +
                  n2*np.outer(mean2 - combined_mean, mean2 - combined_mean))
    return (SS_within + SS_between) / (n1 + n2 - 1)

data1 = [2, 4, 6, 8]
data2 = [10, 12, 14]
print(combined_mean_variance(data1, data2))

X1 = np.array([[1, 2], [2, 3], [3, 4]])
X2 = np.array([[5, 6], [6, 7]])
print(combined_covariance(X1, X2))
