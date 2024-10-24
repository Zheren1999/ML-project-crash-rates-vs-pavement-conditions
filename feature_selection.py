import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_csv('pav_crash_data_cleaned.csv')


feature_columns = ["PCI_2", "PAVTYP", "RUT_INDX", "FAULT_INDX", "CRACK_INDX", "FRICT", "A_INDX", "AADT", "SPEED"]


for col in feature_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')


data = pd.get_dummies(data, columns=["PAVTYP"], drop_first=True)


feature_columns = [col for col in data.columns if col != 'crash_count']


X = data[feature_columns]
y = data['crash_count']


X = X.dropna()
y = y[X.index]  

def forward_selection(X, y):
    selected = []  
    remaining = list(X.columns)  
    while len(remaining) != 0:
        best_pvalue = float('inf')
        best_feature = None
        for feature in remaining:
            model_features = selected + [feature]
            X_train = sm.add_constant(X[model_features])  
            model = sm.GLM(y, X_train, family=sm.families.NegativeBinomial()).fit()  
            pvalue = model.pvalues[feature]  
            if pvalue < best_pvalue:
                best_pvalue = pvalue
                best_feature = feature
        if best_feature:
            selected.append(best_feature)
            remaining.remove(best_feature)
            print(f"Selected Feature: {best_feature}, p-value: {best_pvalue}")
        else:
            break  
    return selected


selected_features = forward_selection(X, y)
print("Final Selected Features:", selected_features)
