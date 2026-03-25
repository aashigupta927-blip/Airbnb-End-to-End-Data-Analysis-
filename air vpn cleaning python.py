# import pandas as pd
# import os

# # RAW data folder path
# input_folder = input("Enter RAW folder path: ").strip().replace('"','')

# # New Clean folder (Desktop par banega)
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
# output_folder = os.path.join(desktop, "Task2 Airbnb NYC Clean Data Folder")

# # Create clean folder
# os.makedirs(output_folder, exist_ok=True)

# print("\nProcessing files...\n")

# for file in os.listdir(input_folder):

#     file_path = os.path.join(input_folder, file)

#     try:
#         # CSV file
#         if file.endswith(".csv"):
#             print("Cleaning CSV:", file)
#             df = pd.read_csv(file_path, low_memory=False)

#         # JSON file
#         elif file.endswith(".json"):
#             print("Converting JSON:", file)
#             df = pd.read_json(file_path)
#             file = file.replace(".json", ".csv")

#         else:
#             continue

#         print("Original Shape:", df.shape)

#         # Remove duplicates
#         df = df.drop_duplicates()

#         # Remove blank rows
#         df = df.dropna(how="all")

#         # Clean column names
#         df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#         # Clean text columns
#         for col in df.select_dtypes(include=["object"]):
#             df[col] = df[col].astype(str).str.strip()

#         print("Cleaned Shape:", df.shape)

#         # Save cleaned file
#         save_path = os.path.join(output_folder, file)
#         df.to_csv(save_path, index=False)

#         print("Saved to:", save_path, "\n")

#     except Exception as e:
#         print("Error processing", file, ":", e)

# print("\nAll files cleaned successfully!")
# print("Clean files saved here:", output_folder)

# import pandas as pd
# import json
# import os

# # GeoJSON file path
# file_path = input("Enter GeoJSON file path: ").strip().replace('"','')

# # Clean folder path
# output_folder = r"C:\Users\hp\OneDrive\Documents\Task2 Airbnb NYC Clean Data Folder"

# # Output file name
# output_file = os.path.join(output_folder, "clean_neighbourhoods.csv")

# try:
#     # Load GeoJSON
#     with open(file_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     features = data["features"]

#     rows = []
#     for feature in features:
#         rows.append(feature["properties"])

#     df = pd.DataFrame(rows)

#     print("Original Shape:", df.shape)

#     # Remove duplicates
#     df = df.drop_duplicates()

#     # Remove blank rows
#     df = df.dropna(how="all")

#     # Clean column names
#     df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#     # Clean text columns
#     for col in df.select_dtypes(include=["object"]):
#         df[col] = df[col].astype(str).str.strip()

#     print("Cleaned Shape:", df.shape)

#     # Save CSV in Clean Data Folder
#     df.to_csv(output_file, index=False)

#     print("\nFile successfully saved!")
#     print("Location:", output_file)

# except Exception as e:
#     print("Error:", e)

# import pandas as pd

# # Load dataset
# df = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\Task2 Airbnb NYC Clean Data Folder\listings_summary.csv")

# print(df.shape)
# print(df.head())
# print(df.info())

# Remove $ sign from price
# df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
# # Handle missing values
# df = df.dropna(subset=['price'])

# # Remove extreme prices (outliers)
# df = df[df['price'] < 1000]

# import pandas as pd

# listings = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\Task2 Airbnb NYC Clean Data Folder\listings_summary.csv")

# reviews = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\Task2 Airbnb NYC Clean Data Folder\reviews_summary.csv")

# merged = pd.merge(
#     listings,
#     reviews,
#     left_on="id",
#     right_on="listing_id",
#     how="left"
# )

# merged.to_csv(r"C:\Users\hp\OneDrive\Documents\Task2 Airbnb NYC Clean Data Folder\airbnb_final_dataset.csv", index=False)

# print("Dataset merged successfully")

# import os

# path = r"C:\Users\hp\OneDrive\Documents\Task2 Airbnb NYC Clean Data Folder"

# print(os.listdir(path))

import pandas as pd
import numpy as np

# 1️⃣ Load dataset
df = pd.read_csv("C:/Users/hp/OneDrive/Documents/Task2 Airbnb NYC Clean Data Folder/airbnb_final_dataset.csv")

# 2️⃣ Basic info check
print(df.info())
print(df.head())

# 3️⃣ Remove duplicate rows
df = df.drop_duplicates()

# 4️⃣ Handle missing values
df = df.replace("", np.nan)

# Example: fill or drop nulls
df = df.dropna(subset=['price'])  # important column
df = df.fillna(0)

# 5️⃣ Clean PRICE column (remove $, commas etc.)
if 'price' in df.columns:
    df['price'] = df['price'].astype(str)
    df['price'] = df['price'].str.replace(r'[$,]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 6️⃣ Convert other numeric columns safely
numeric_cols = ['minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365']

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 7️⃣ Remove rows with conversion errors
df = df.dropna()

# 8️⃣ Reset index
df = df.reset_index(drop=True)

# 9️⃣ Final check
print(df.info())

# 🔟 Save cleaned file
df.to_csv("cleaned_airbnb_dataset.csv", index=False)

print("✅ Data cleaning done and file saved!")

