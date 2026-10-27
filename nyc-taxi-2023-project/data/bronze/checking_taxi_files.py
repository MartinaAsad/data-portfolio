
import pyarrow.parquet as pq
from pathlib import Path

folder = Path("data/bronze/taxis")

# January schema as reference
reference_path = folder / "yellow_tripdata_2023-01.parquet"
reference_schema = pq.read_schema(reference_path)

for month in range(2, 13):

    filename = f"yellow_tripdata_2023-{month:02d}.parquet"
    filepath = folder / filename

    current_schema = pq.read_schema(filepath)

    print(f"\nMONTH {month:02d}")

    # Compare column names
    reference_cols = set(reference_schema.names)
    current_cols = set(current_schema.names)

    print("Missing columns:", reference_cols - current_cols)
    print("Extra columns:", current_cols - reference_cols)

    # Compare data types
    for col in reference_cols & current_cols:

        ref_type = reference_schema.field(col).type
        curr_type = current_schema.field(col).type

        if ref_type != curr_type:
            print(
                f"{col}: {ref_type} -> {curr_type}"
            )
