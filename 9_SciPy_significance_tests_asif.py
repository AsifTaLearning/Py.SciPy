import numpy as np
from scipy.stats import ttest_ind , kstest , describe , skew , kurtosis , normaltest

"""
    Hypothesis in Statistics
    Hypothesis is an assumption about a parameter in population.

    Null Hypothesis
    It assumes that the observation is not statistically significant.

    Alternate Hypothesis
    It assumes that the observations are due to some reason.

    It's alternate to Null Hypothesis.

    One tailed test
    When our hypothesis is testing for one side of the value only, it is called "one tailed test".

    Two tailed test
    When our hypothesis is testing for both side of the values.

    Alpha value
    Alpha value is the level of significance.

    P value
    P value tells how close to extreme the data actually is.
    
    """


# SciPy Statistical Significance Tests
# T-Test

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)

# Another example

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2).pvalue

print(res)

# KS-Test

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)

# Statistical Description of Data

v = np.random.normal(size=100)
res = describe(v)

print(res)

# Normality Tests (Skewness and Kurtosis)

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

# Another example

v = np.random.normal(size=100)

print(normaltest(v))





