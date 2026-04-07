import pandas as pd

# Read dataset
df = pd.read_csv("data/etl_job_logs.csv")

# Convert to datetime
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

# Calculate duration
df['duration_mins'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60

# Identify delayed jobs (>30 mins)
df['is_delayed'] = df['duration_mins'] > 30

# Print result
print(df)

# Save output
df.to_csv("output/processed_etl_logs.csv", index=False)
