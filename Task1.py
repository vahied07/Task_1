import pandas as pd

file_path = r"C:\Users\jagad\OneDrive\Documents\sales_data.csv"
df = pd.read_csv(file_path)

df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
df['store_id'].fillna("0", inplace=True)

df.rename(columns={
    'order_id': 'Order_ID',
    'order_date': 'Order_Date',
    'customer_id': 'Customer_ID',
    'product_id': 'Product_ID',
    'store_id': 'Store_ID',
    'sales_channel': 'Sales_Channel',
    'quantity': 'Quantity',
    'unit_price': 'Unit_Price',
    'discount_pct': 'Discount_PCT',
    'total_amount': 'Total_Amount'
}, inplace=True)

text_columns = df.select_dtypes(include='object').columns.tolist()
df[text_columns] = df[text_columns].apply(lambda x: x.str.strip().str.title())

date_columns = [col for col in df.columns if 'date' in col.lower()]
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')

output_path = r"C:\Users\jagad\OneDrive\Documents\sales_data_cleaned1.csv"
df.to_csv(output_path, index=False)

print("✅ Data cleaned successfully. Preview:")
print(df.head())





