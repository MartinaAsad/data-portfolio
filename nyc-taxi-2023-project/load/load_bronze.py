import os
from pathlib import Path

def df_to_parquet(df, output_dir, file):
    
    #create folder if it's not exist
    os.makedirs(output_dir, exist_ok=True)
    
    filename = Path(output_dir) / file
    df.to_parquet(filename, engine='pyarrow', compression='snappy', index=False)

