import statsmodels.api as sm
import pandas as pd

def negative_binomial_regression(X, y):
    model = sm.GLM(y, X, family=sm.families.NegativeBinomial()).fit()
    print(model.summary())
    return model