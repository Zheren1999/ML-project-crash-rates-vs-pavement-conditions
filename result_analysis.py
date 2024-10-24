import matplotlib.pyplot as plt
import pandas as pd

def plot_residuals(model, X, y):
    residuals = y - model.predict(X)
    plt.figure(figsize=(10, 6))
    plt.scatter(model.predict(X), residuals)
    plt.axhline(0, color='red', linestyle='--')
    plt.title('Residual Plot')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.show()

def feature_importance(model):
    importance = pd.Series(model.params, index=model.model.exog_names)
    print(importance.sort_values(ascending=False))
