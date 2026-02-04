def transform_data(df):
    df = df.dropna()
    df["order_date"] = df["order_date"].astype(str)
    df["total_price"] = df["price"] * df["quantity"]
    return df
