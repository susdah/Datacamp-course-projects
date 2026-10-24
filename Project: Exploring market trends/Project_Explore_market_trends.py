# Import necessary packages
import pandas as pd
import numpy as np

# Import the three files into dataframes
price_df = pd.read_csv("data/airbnb_price.csv")
room_type_df = pd.read_excel("data/airbnb_room_type.xlsx")
last_review_df = pd.read_csv("data/airbnb_last_review.tsv", sep="\t")

# Merge the three on the listing_id column
airbnb_data = price_df.merge(room_type_df, on="listing_id") \
                      .merge(last_review_df, on="listing_id")

# Clean the price column and convert it to int
airbnb_data["price"] = airbnb_data["price"].str.replace(" dollars", "").astype(int)

# Clean the last review column and convert it to a yy-mm-dd format
airbnb_data["last_review"] = pd.to_datetime(airbnb_data['last_review'], format='%B %d %Y')

# Clean the room type column and make it into categories
dict_map = {'entire home/apt':'Entire home/apt',
            'ENTIRE HOME/APT':'Entire home/apt',
            'private room':'Private room',
            'PRIVATE ROOM':'Private room',
            'shared room':'Shared room',
            'SHARED ROOM':'Shared room'}
airbnb_data["room_type"] = airbnb_data["room_type"].replace(dict_map)

# 1. What are the dates of the earliest and most recent reviews?
earliest_review = airbnb_data["last_review"].min()
latest_review = airbnb_data["last_review"].max()

# 2. How many of the listings are private rooms?
private_room_count = airbnb_data["room_type"].str.count("Private room").sum()

# 3. What is the average listing price?
average_list_price = round(airbnb_data["price"].mean(), 2)

# 4. Combine the new variables into one DataFrame
review_dates = pd.DataFrame({
    "first_reviewed" : [earliest_review],
    "last_reviewed" : [latest_review],
    "nb_private_rooms" : [private_room_count],
    "avg_price" : [average_list_price]
})
print(review_dates)
