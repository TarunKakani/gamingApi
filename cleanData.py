import pandas as pd

df = pd.read_csv("books_cleaned.csv")
# print(df.columns.tolist())

# # remove columns with specific names
# df = df.drop(columns=["isbn13", "language_code", "ratings_count", "text_reviews_count"])

# # save csv
# df.to_csv("books_cleaned.csv", index=False)