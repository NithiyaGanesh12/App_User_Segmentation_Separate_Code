# Load data
raw=demo_data() if DATA_PATH is None else pd.read_csv(DATA_PATH).rename(columns=COLUMN_MAPPING)
if raw.columns.duplicated().any(): raise ValueError('Duplicate columns after mapping')
print('SYNTHETIC DEMONSTRATION' if DATA_PATH is None else DATA_PATH)
display(raw.head())
raw.info()
