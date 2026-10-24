# Import required modules
import pandas as pd
import numpy as np
from statsmodels.formula.api import logit
from sklearn.metrics import confusion_matrix

# Goal: To identify which feature procudes the best accuracy in predicting future claims.

# 1. Read in the csv and explore the data.
car_insurance = pd.read_csv("car_insurance.csv")
print(car_insurance.columns)
print(car_insurance.dtypes)

# 2a. Check which columns has missing values and amend by filling in the median value of the column.
#print(car_insurance.isna().sum())
car_insurance["credit_score"].fillna(car_insurance["credit_score"].median(), inplace=True)
car_insurance["annual_mileage"].fillna(car_insurance["annual_mileage"].median(), inplace=True)
#print(car_insurance.isna().sum())

# 2b. Fix the data types in the columns that are wrong now that the NaN's are fixed.
car_insurance[["vehicle_ownership", "married", "children", "annual_mileage", "outcome"]] = car_insurance[["vehicle_ownership", "married", "children", "annual_mileage", "outcome"]].astype(int)
#print(car_insurance.dtypes()

# 3. Make a list with all the features to model, then run a for loop to model them using logit()
all_models = []
columns = list(car_insurance.columns[1:-1])

for i in columns:
    this_model = logit(f"outcome ~ {i}", data=car_insurance).fit()
    all_models.append(this_model)

# 4. Measure performance with np.round() and confusion metrix
actual_outcomes = car_insurance["outcome"]
all_model_accuracies = []

from sklearn.metrics import confusion_matrix

# Loop over all_models, compare the results and confusion matrix.
for i in all_models:
    # Predict the outcome
    predicted_outcome = (i.predict(car_insurance) >= 0.5).astype(int)
    # Use the imported confusion_matrix as that is easier than what is in the course
    # Documentation: https://scikit-learn.org/stable/api/sklearn.metrics.html
    conf_matrix = confusion_matrix(actual_outcomes, predicted_outcome)
    TN, FP, FN, TP = conf_matrix.ravel()
    # Calculate the accuracy and append to the list
    accuracy = (TN + TP) / (TN + FN + FP + TP)
    all_model_accuracies.append(accuracy)

print(all_model_accuracies)

# 5. Measure which one is best

best_accuracy = max(all_model_accuracies)
best_model_index = all_model_accuracies.index(best_accuracy)

best_model = all_models[best_model_index]
best_feature_to_measure = best_model.params.index[1].split('[')[0]  # Removed extra parenthesis

best_feature_df = pd.DataFrame({"best_feature":[best_feature_to_measure],
                                "best_accuracy":[best_accuracy]})

print(best_feature_df)
