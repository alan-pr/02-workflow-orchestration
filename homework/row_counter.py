import pandas as pd
from tqdm import tqdm
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <color> <year> [month]")
    print("Example:")
    print("  python script.py yellow 2020")
    print("  python script.py yellow 2020 5")
    sys.exit(1)

color = sys.argv[1]
year = sys.argv[2]
rows = 0

if len(sys.argv) > 3:
    month = int(sys.argv[3])
    file = f"gs://gothic-doodad-479223-j7-bucket/{color}_tripdata_{year}-{month:02}.csv"
    df = pd.read_csv(file)
    rows = len(df)
else:
    months = 12

    for table in tqdm(range(1, months + 1)):
        file = f"gs://gothic-doodad-479223-j7-bucket/{color}_tripdata_{year}-{table:02}.csv"
        df = pd.read_csv(file)
        rows += len(df)

print(f"Total rows: {rows}")