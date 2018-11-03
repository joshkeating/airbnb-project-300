import csv
import pandas as pd
import numpy as np


def load_host_data():
    file_path = '../data/listings.csv'
    return pd.read_csv(file_path)



full_df = load_host_data()

print(list(full_df))

# host_data = full_df['host_id':'host_abput']