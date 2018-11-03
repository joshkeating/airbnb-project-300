import csv
import pandas as pd
import numpy as np


def load_host_data(file_path):
    return pd.read_csv(file_path)


full_df = load_host_data('./data/listings.csv')

host_data = full_df[['host_id', 'host_url', 'host_name', 'host_location', 'host_about']]

print(host_data.head())