import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_correlation_matrix(data):
    plt.figure(figsize=(12, 10))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def box_plot_feature(data, feature):
    sns.boxplot(x=data[feature])
    plt.title(f'Box plot of {feature}')
    plt.show()
