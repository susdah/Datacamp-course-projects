# Import necessary libraries
import pandas as pd

# Load the dataset
ds_jobs = pd.read_csv("customer_train.csv")

# View the dataset
ds_jobs.head()

# Create a copy of ds_jobs for transforming
ds_jobs_transformed = ds_jobs.copy()

#1: Categories with 2 options to booleans:
ds_jobs_transformed["job_change"] = ds_jobs_transformed["job_change"].astype(bool)
ds_jobs_transformed["relevant_experience"] = ds_jobs_transformed["relevant_experience"].astype(bool)

#2: Integers to int32:
ds_jobs_transformed["student_id"] = ds_jobs_transformed["student_id"].astype("int32")
ds_jobs_transformed["training_hours"] = ds_jobs_transformed["training_hours"].astype("int32")

#3: Floats to float16:
ds_jobs_transformed["city_development_index"] = ds_jobs_transformed["city_development_index"].astype("float16")

#5: Ordinal categorical columns must be ordered.
order_education = ["Primary School", "High School", "Graduate", "Masters", "Phd"]
ds_jobs_transformed["education_level"] = ds_jobs_transformed["education_level"].astype(
    pd.CategoricalDtype(order_education, ordered=True)
)

order_experience = ["<1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", ">20"]
ds_jobs_transformed["experience"] = ds_jobs_transformed["experience"].astype(
    pd.CategoricalDtype(order_experience, ordered=True)
)

order_comp_size = ["<10", "10-49", "50-99", "100-499", "500-999", "1000-4999", "5000-9999", ">10000"]
ds_jobs_transformed["company_size"] = ds_jobs_transformed["company_size"].astype(
    pd.CategoricalDtype(order_comp_size, ordered=True)
)

order_last_new_job = ["never", "1", "2", "3", "4", ">4"]
ds_jobs_transformed["last_new_job"] = ds_jobs_transformed["last_new_job"].astype(
    pd.CategoricalDtype(order_last_new_job, ordered=True)
)

order_enrolled = ["no_enrollment", "Part time course", "Full time course"]
ds_jobs_transformed["enrolled_university"] = ds_jobs_transformed["enrolled_university"].astype(
    pd.CategoricalDtype(order_enrolled, ordered=True)
)

#4: Categorical columns to category data types:
cols_to_convert = [
    "city",
    "gender",
    "education_level",
    "major_discipline",
    "experience",
    "company_size",
    "company_type",
    "last_new_job"
]
# Only convert those not already set as CategoricalDtype above
for col in cols_to_convert:
    if not pd.api.types.is_categorical_dtype(ds_jobs_transformed[col]):
        ds_jobs_transformed[col] = ds_jobs_transformed[col].astype("category")

#6: Get out students with 10+ years exp, 1000 empl comp.
ds_jobs_transformed = ds_jobs_transformed[(ds_jobs_transformed['experience'] >= '10') & (ds_jobs_transformed['company_size'] >= '1000-4999')]
