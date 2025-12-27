import pandas as pd
import sys

# --- 1. Define the Consolidated IOC Data ---
# This data is extracted and cleaned from the IOCs.txt content for accurate spreadsheet generation.

# Hashes data is explicitly structured to include the type and a comment for clarity.
HASH_DATA = [
    {"Type": "SHA256", "Value": "f8c452c4b594ec27577b117c7e7d388ae702df5f6d6affdcc4a0e49ea0f7a",
     "Comment": "Primary sample"},
    {"Type": "MD5", "Value": "c66f4cb55cea8acd289562ba3b06f56d", "Comment": "Cuckoo/Primary Analysis"},
    {"Type": "MD5", "Value": "186c4a0344b1c7022066d03f0d23805c", "Comment": "VT/Any.run Secondary (Related file)"},
    {"Type": "SHA1", "Value": "cb6a71bb42fbf5f4ca1d06e7e6d074e78cdf728a0", "Comment": "Primary sample"}
]

# Updated DOMAIN_DATA to include the full search URLs exactly as they appeared in the analysis.
DOMAIN_DATA = [
    "https://www.google.com/search?q=cdn.discordapp.com",
    "https://www.google.com/search?q=settings-win.data.microsoft.com",
    "https://www.google.com/search?q=crl.microsoft.com",
    "https://www.google.com/search?q=login.live.com",
    "https://www.google.com/search?q=ocsp.digicert.com",
    "https://www.google.com/search?q=client.wns.windows.com",
    "https://www.google.com/search?q=slscr.update.microsoft.com",
    "www.microsoft.com",
    "https://www.google.com/search?q=fe3cr.delivery.mp.microsoft.com"
]

IP_DATA = [
    "162.159.135.233",
    "51.104.136.2",
    "51.101.42.42",
    "51.101.78.42",
    "51.124.78.146",
    "40.126.32.68",
    "23.63.118.230",
    "172.211.123.248",
    "40.127.240.158",
    "74.178.76.128",
    "2.23.246.101",
    "13.95.31.18",
    "4.154.209.85",
    "192.168.100.255"
]

FILENAME_DATA = [
    "x.exe",
    "CW1Sample1null.unknown.exe",
    "Sample.exe",
    "Winlogon.dll"
]

REGISTRY_DATA = [
    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\svchost.exe"
]


def export_iocs_to_excel(filename="malware_iocs.xlsx"):
    """
    Creates an Excel file with multiple sheets, each containing a category of IOCs.
    """
    print(f"[*] Starting export to {filename}...")

    try:
        # Create DataFrames
        df_hashes = pd.DataFrame(HASH_DATA)
        df_domains = pd.DataFrame({"Domain or Search URL": DOMAIN_DATA})  # Updated column name to reflect search URLs
        df_ips = pd.DataFrame({"IP Address": IP_DATA})
        df_files = pd.DataFrame({"Filename": FILENAME_DATA})
        df_registry = pd.DataFrame({"Registry Key": REGISTRY_DATA})

        # Create a Pandas Excel writer, relying on the installed 'openpyxl' engine
        # We rely on openpyxl being installed, which your previous output confirmed.
        with pd.ExcelWriter(filename) as writer:

            # --- Write DataFrames to different sheets ---
            df_hashes.to_excel(writer, sheet_name='Hashes', index=False)
            df_domains.to_excel(writer, sheet_name='Domains', index=False)
            df_ips.to_excel(writer, sheet_name='IP Addresses', index=False)
            df_files.to_excel(writer, sheet_name='Filenames', index=False)
            df_registry.to_excel(writer, sheet_name='Registry Keys', index=False)

            # --- Apply formatting (optional but good practice) ---
            # Using openpyxl for auto-sizing columns
            from openpyxl.utils import get_column_letter

            for sheet_name in writer.sheets:
                worksheet = writer.sheets[sheet_name]

                # Iterate through all columns in the worksheet
                for col in worksheet.columns:
                    max_length = 0
                    column = col[0].column  # Get the column index (1-based)

                    # Iterate through all cells in the column to find the max length
                    for cell in col:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except (TypeError, ValueError):
                            pass

                    # Set the column width, adding a buffer of 2
                    adjusted_width = max_length + 2
                    worksheet.column_dimensions[get_column_letter(column)].width = adjusted_width

            print(f"[+] Successfully exported {filename} with 5 sheets.")

    # Catch a general exception and print the actual error for better debugging
    except Exception as e:
        print(
            f"\n[!] An error occurred during export. Please ensure pandas and openpyxl are installed and try again: {e}")
        sys.exit(1)


if __name__ == "__main__": export_iocs_to_excel()