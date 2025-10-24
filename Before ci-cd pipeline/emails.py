import pandas as pd
import re

# --- Step 1: Read your CSV file ---
df = pd.read_csv("cc2.csv")

# --- Step 2: Get the roll number column ---
roll_numbers = df['Roll no ']

emails = []

for roll in roll_numbers:
    if pd.isna(roll):  # skip blank cells
        emails.append("")
        continue

    roll = str(roll).strip().upper()
    roll = re.sub(r'[^A-Z0-9]', '', roll)  # remove junk characters

    # --- Step 3: Match F or P variants ---
    match = re.search(r'(\d{2})([FP])(\d{3,4})', roll)
    if match:
        year, campus, num = match.groups()
        num = num.zfill(4)
        email = f"{campus.lower()}{year}{num}@cfd.nu.edu.pk"
        emails.append(email)
    else:
        # if the format is broken but still contains numbers, try to extract something
        fallback = re.findall(r'\d+', roll)
        if len(fallback) >= 2:
            year = fallback[0][-2:]  # grab last 2 digits for year
            num = fallback[-1].zfill(4)
            email = f"f{year}{num}@cfd.nu.edu.pk"
            emails.append(email)
        else:
            emails.append("")

# --- Step 4: Add emails and export ---
df['Email'] = emails
df.to_csv("roll_numbers_with_emails_clean.csv", index=False)

# --- Step 5: Summary ---
valid_count = sum(1 for e in emails if e and "@cfd.nu.edu.pk" in e)
print(f"✅ Successfully generated {valid_count} valid emails.")
print("📁 Saved file: roll_numbers_with_emails_clean.csv")