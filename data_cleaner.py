import pandas as pd
from pathlib import Path
import sys

def clean_csv(input_path: str, output_path: str | None = None):
    """Clean and normalize a CSV file."""
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    print(f"📂 Reading: {input_file.name}")
    df = pd.read_csv(input_file)

    # Drop completely empty rows
    before = len(df)
    df.dropna(how="all", inplace=True)
    print(f"🧽 Dropped {before - len(df)} empty rows")

    # Drop duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    print(f"🧹 Dropped {before - len(df)} duplicate rows")

    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Clean up textual columns (if any)
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

        # Normalize specific fields
        if "name" in col:
            df[col] = df[col].str.title()
        elif "email" in col:
            df[col] = df[col].str.lower()

    # Decide output path
    if output_path is None:
        output_path = input_file.with_name(f"{input_file.stem}_clean.csv")

    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned file saved as: {output_path}")
    return df


if __name__ == "__main__":
    # Usage: python data_cleaner.py cs.csv
    input_file = sys.argv[1] if len(sys.argv) > 1 else "cs.csv"
    clean_csv(input_file)