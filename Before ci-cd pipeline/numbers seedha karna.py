import re
import pandas as pd


def normalize_number(num):
    num = str(num)
    num = re.sub(r'[^0-9]', '', num)  # remove non-digits

    if num.startswith('92'):
        num = '0' + num[2:]
    elif num.startswith('3'):
        num = '0' + num
    # Now ensure format 03xx-xxxxxxx
    if len(num) == 11:
        num = num[:4] + '-' + num[4:]
    return num


df = pd.read_excel("C://Users/gamer/OneDrive/Documents/Book2.xlsx")
df['Normalized'] = df['Phone'].apply(normalize_number)
df.to_excel("normalized_numbers.xlsx", index=False)