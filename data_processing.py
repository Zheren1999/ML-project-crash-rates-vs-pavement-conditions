import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, low_memory=False)

    imp_data = df[[ 'PMISYR', 'SYSTEM', 'PAVTYP', 'CONYR', 'RESYR', 'PMIS_LENGTH',
                    'LANE_MILES', 'PCI_2', 'RUT_INDX', 'IRI_INDX', 'FAULT_INDX', 'CRACK_INDX',
                    'IRI', 'FRICT', 'FAULT', 'FAULTAV', 'RUT', 'CRACK_RATIO', 'T_INDX',
                    'AADT', 'TRUCKS', 'LANES', 'SPEED', 'SURFACE_TYPE', 'PAVTHICK',
                    'TACCDPTH', 'TPCCDPTH', 'BASEDPTH', 'TREATMENT', 'crash_count']]

    threshold = len(df) * 0.7
    imp_cleaned = imp_data.dropna(axis=1, thresh=threshold)

    columns_to_fill = ['PMIS_LENGTH', 'LANE_MILES', 'PCI_2', 'IRI_INDX', 'CRACK_INDX', 'IRI']
    column_means = imp_cleaned[columns_to_fill].mean()

    for col in columns_to_fill:
        imp_cleaned.loc[imp_cleaned[col].isnull(), col] = column_means[col]
    
    imp_cleaned = imp_cleaned.dropna()
    imp_cleaned.to_csv("final_cleaned_data01.csv", index=False)
    return imp_cleaned