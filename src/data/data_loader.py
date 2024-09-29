import pandas as pd

def load_data(filepath):
    """loading dataset"""
    return pd.read_csv(filepath)