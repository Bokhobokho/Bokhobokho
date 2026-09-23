import pandas as pd
import os
import glob
# Folder containing the CSV files
folder = os.path.expanduser("~/work/tables/without_site_id")
# Output file
output_file = os.path.join(folder, "combined.csv")
# Find all CSV files
csv_files = glob.glob(os.path.join(folder, "*.csv"))
# Don't include combined.csv if it already exists
csv_files = [
    file for file in csv_files
    if os.path.abspath(file) != os.path.abspath(output_file)
]
print("=" * 70)
print("CSV COMBINATION")
print("=" * 70)
print(f"Folder: {folder}")
print(f"CSV files found: {len(csv_files)}")
print()
dataframes = []
for file in csv_files:
    print(f"Reading: {os.path.basename(file)}")
    try:
        df = pd.read_csv(file)
        dataframes.append(df)
        print(f"  Rows: {len(df):,}")
        print(f"  Columns: {len(df.columns)}")
    except Exception as e:
        print(f"  ERROR: {e}")
# Combine all files
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)
    # Save
    combined_df.to_csv(output_file, index=False)
    print()
    print("=" * 70)
    print("COMBINATION COMPLETE")
    print("=" * 70)
    print(f"Files combined : {len(dataframes):,}")
    print(f"Total rows     : {len(combined_df):,}")
    print(f"Total columns  : {len(combined_df.columns):,}")
    print(f"Output file    : {output_file}")
else:
    print("No CSV files found.")
