import pandas as pd
import os

def clean_data():
    input_path = '/opt/airflow/data/raw/superstore_dataset2011-2015.csv'
    output_path = '/opt/airflow/data/processed/cleaned_data.csv'

    df = pd.read_csv(input_path, encoding='ISO-8859-1')
    df.dropna(subset=['Order ID', 'Order Date', 'Sales', 'Profit'], inplace=True)

    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
    df['Shipping Cost'] = pd.to_numeric(df['Shipping Cost'], errors='coerce')
    df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
    df['Profit Margin'] = (df['Profit'] / df['Sales']).round(2)

    df.dropna(inplace=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
