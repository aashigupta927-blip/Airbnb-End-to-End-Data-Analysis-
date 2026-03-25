import pandas as pd

# Load file
file_path = input("Enter your CSV file path: ")
df = pd.read_csv(file_path, low_memory=False)

print("Original Shape:", df.shape)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Remove completely blank rows
df = df.dropna(how='all')

# 3. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 4. Fix numeric columns (VERY IMPORTANT)
numeric_cols = [
    'id', 'host_id', 'price', 'minimum_nights',
    'number_of_reviews', 'reviews_per_month',
    'calculated_host_listings_count', 'availability_365'
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Remove rows where critical IDs are missing
df = df.dropna(subset=['id', 'host_id'])

# 6. Fill remaining numeric nulls
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# 7. Clean text columns
text_cols = ['name', 'host_name', 'neighbourhood_group', 'neighbourhood', 'room_type', 'city', 'street', 'state']

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# 8. Fix date column
if 'last_review' in df.columns:
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

# 9. Final shape
print("Cleaned Shape:", df.shape)

# 10. Save file
save_path = input("Enter path to save cleaned file (.csv): ")
df.to_csv(save_path, index=False)

print("✅ Clean file saved successfully!") 