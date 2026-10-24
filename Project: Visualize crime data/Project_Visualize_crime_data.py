# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import the file.
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes.head()
crimes.dtypes

# Extract hour as string (first two characters)
crimes["hour"] = crimes["TIME OCC"].str[:2].astype(int)

# Find the most common hour.
peak_crime_hour = int(crimes["hour"].mode()[0])
sns.countplot(data=crimes, x="hour")
plt.show()

# Filter for night time crimes (between 10 PM and 3 AM)
night_time = crimes[crimes["hour"].isin([22,23,0,1,2,3])]

# Group by "AREA NAME" and count occurrences, filtering for the largest value and saving the "AREA NAME"
peak_night_crime_location = night_time.groupby("AREA NAME",
                                               as_index=False)["hour"].count().sort_values("hour",
                                                ascending=False).iloc[0]["AREA NAME"]
# Print the peak night crime location
print(f"The area with the largest volume of night crime is {peak_night_crime_location}")

# Filter crimes by victim age groups.
bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
crimes["age bracket"] = pd.cut(crimes["Vict Age"], bins=bins, labels=labels)
victim_ages = crimes["age bracket"].value_counts()
print(victim_ages)
sns.countplot(data=crimes, x="age bracket")
plt.show()

