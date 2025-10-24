import pandas as pd
from pathlib import Path
import sys
import re

def clean_csv(input_path: str, output_path: str | None = None):
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"❌ File not found: {input_file}")

    print(f"📥 Reading: {input_file.name}")
    df = pd.read_csv(input_file)

    # Drop all "Unnamed:" columns (they're just garbage)
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Replace any literal "NaN", "nan", or blanks with actual NaN
    df.replace(["NaN", "nan", "NAN", "Nan", " "], pd.NA, inplace=True)

    # Clean up each column
    if "name" in df.columns:
        df["name"] = (
            df["name"]
            .astype(str)
            .str.strip()
            .str.title()
            .replace("Nan", pd.NA)
        )

    if "roll_no_(eg:25f-1234)" in df.columns:
        df.rename(columns={"roll_no_(eg:25f-1234)": "roll_no"}, inplace=True)
        df["roll_no"] = (
            df["roll_no"]
            .astype(str)
            .str.strip()
            .str.upper()
            .apply(lambda x: re.sub(r"\.0$", "", x))
        )

    if "batch" in df.columns:
        df["batch"] = (
            df["batch"]
            .astype(str)
            .str.replace(".0", "", regex=False)
            .str.strip()
        )

    if "contact_no_(whatsapp)" in df.columns:
        df.rename(columns={"contact_no_(whatsapp)": "contact_no"}, inplace=True)
        df["contact_no"] = df["contact_no"].astype(str).str.strip()

    if "past_experience_(if_any)" in df.columns:
        df.rename(columns={"past_experience_(if_any)": "past_experience"}, inplace=True)
        df["past_experience"] = df["past_experience"].fillna("No").astype(str).str.strip()

    if "preferred_team" in df.columns:
        df["preferred_team"] = df["preferred_team"].astype(str).str.title().str.strip()

    # Drop fully empty rows
    df.dropna(how="all", inplace=True)

    # Remove duplicate entries by roll_no if available
    if "roll_no" in df.columns:
        before = len(df)
        df.drop_duplicates(subset=["roll_no"], inplace=True)
        print(f"🧹 Removed {before - len(df)} duplicate roll numbers")

    # Clean up whitespaces across all string columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    # Prepare output file
    if output_path is None:
        output_path = input_file.with_name(f"{input_file.stem}_clean_final.csv")

    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned CSV saved as: {output_path}")
    print(f"📊 Final shape: {df.shape}")
    return df


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "cs_clean.csv"
    clean_csv(input_file)