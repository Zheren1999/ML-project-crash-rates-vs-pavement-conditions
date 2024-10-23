# Crash Prediction and Pavement Quality Analysis

## Overview

This project investigates the relationship between pavement characteristics and the frequency of traffic accidents using machine learning techniques. The primary goal is to identify significant pavement features that can assist transportation agencies in improving road safety by preventing accident crashes. The study utilizes Negative Binomial Regression, exploring how pavement conditions, traffic data, and other factors influence crash occurrences on the Iowa road network.

## Data Sources

The data used in this project was obtained from the Iowa Department of Transportation (IowaDOT) and includes:

- **Crash Data (2009-2013):** Information about accident location, date, severity, and type.
- **Pavement Quality Data (2009-2013):** Mile-by-mile pavement roughness, surface information, and other related metrics.

The crash dataset contains 50 features with 77,314 observations, while the pavement dataset contains 234 features with 4,119 observations.

## Methodology

### Data Preprocessing

- **Data Cleaning:** Missing values were handled, duplicates removed, and data formats standardized.
- **Feature Selection:** The Boruta algorithm was used to trim down the dataset to 9 significant features.
- **Data Merging:** GIS software (QGIS) was used to map crash and pavement data onto a unified dataset.

### Modeling Approach

- **Negative Binomial Regression:** This was used to model overdispersed crash count data. The results identified important factors influencing crash occurrences.
- **Feature Selection:** A total of 9 significant features were identified, including PMIS length, IRI, AADT, and pavement type.

## Key Results

- **Friction Index (FRICT):** Higher friction values reduce the number of crashes.
- **Roughness Index (IRI):** Roads with a higher roughness index have fewer crashes.
- **Pavement Type:** Certain pavement types, such as composite and asphalt, show a lower crash rate compared to concrete pavement.

## Code Structure

- **`data_processing.py`:** Script to clean and merge the crash and pavement datasets.
- **`feature_selection.py`:** Implementation of the Boruta algorithm for feature selection.
- **`modeling.py`:** Implementation of the Negative Binomial Regression model.
- **`visualization.py`:** Script to generate correlation plots and box plots for data visualization.
- **`results_analysis.py`:** Analyzes model results, including residual plots and feature significance.

## Installation and Usage

### Prerequisites

Ensure you have the following libraries installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `geopandas` (for mapping)
- `qgis` (for GIS data manipulation)

To install the required Python packages, you can use the following command:

```bash
pip install -r requirements.txt
```
## Running the Project

### Clone the repository:

```bash
git clone https://github.com/yourusername/crash-prediction-pavement-analysis.git
```

### Navigate to the project directory:
\`\`\`bash
cd crash-prediction-pavement-analysis
\`\`\`

### Run the data preprocessing script:
\`\`\`bash
python data_processing.py
\`\`\`

### Run the feature selection process:
\`\`\`bash
python feature_selection.py
\`\`\`

### Fit and evaluate the regression model:
\`\`\`bash
python modeling.py
\`\`\`
