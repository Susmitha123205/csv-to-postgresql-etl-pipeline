from extract import extract_csv
from transform import transform_data
from load import load_to_db

df = extract_csv("../data/raw_sales.csv")
df_clean = transform_data(df)
load_to_db(df_clean)

print("ETL Pipeline executed successfully")
