
from pathlib import Path


def df_to_parquet(df, output_dir, file):
    
    filename= Path(output_dir)/file
    
    #create folder if it's not exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    df.to_parquet(filename, engine='pyarrow', compression='snappy', index=False)

