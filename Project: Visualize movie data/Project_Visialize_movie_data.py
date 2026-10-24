# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Find the content that is movies.
movies = netflix_df[netflix_df["type"] == "Movie"]

# Find the movies released in the 1990s.
movies_1990s = movies[(movies["release_year"] >= 1990) & (movies["release_year"] <= 1999)].copy()

# Ensure the "duration" column is a str.
movies_1990s["duration"] = movies_1990s["duration"].astype(str)

# Extract the numeric part of the duration and convert to a float.
movies_1990s["duration_minutes"] = movies_1990s["duration"].str.extract('(\d+)').astype(float)

# Get the durations as a Series.
durations = movies_1990s["duration_minutes"]

# Get the most common duration
duration = int(durations.mode())

# Get the action movies from the 1990s.
action_movies = movies_1990s[movies_1990s["genre"].str.contains("Action", na=False)]

# Count how many action movies have duration less than 90 minutes
short_movie_count = (action_movies["duration_minutes"] < 90).sum()

# Make a histogram.
import matplotlib.pyplot as plt
plt.hist(durations.dropna(), bins=20)
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.title("Distribution of Movie Durations (1990s)")
plt.show()
