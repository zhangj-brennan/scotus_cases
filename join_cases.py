import pandas as pd

file_new = "SCDB_Legacy_07_caseCentered_Citation.csv"
file_legacy = "SCDB_2025_01_caseCentered_Citation.csv"

# --- safe reader ---
def read_csv_safe(path):
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")

df_legacy = read_csv_safe(file_legacy)
df_new = read_csv_safe(file_new)

print("Legacy rows:", len(df_legacy))
print("New rows:", len(df_new))

# --- ensure same columns ---
# (this prevents issues if one file has an extra column)
all_columns = sorted(set(df_legacy.columns).union(set(df_new.columns)))

df_legacy = df_legacy.reindex(columns=all_columns)
df_new = df_new.reindex(columns=all_columns)

# --- append (this is what you want) ---
df_all = pd.concat([df_legacy, df_new], ignore_index=True)

print("Combined rows (before dedupe):", len(df_all))

# --- optional: remove exact duplicate rows ---
df_all = df_all.drop_duplicates()

print("Combined rows (after exact dedupe):", len(df_all))

# --- optional: if you want 1 row per case ---
# df_all = df_all.drop_duplicates(subset=["caseId"], keep="last")

# --- sort (optional but nice) ---
df_all = df_all.sort_values(by=["term", "caseId"])

# --- save ---
output_file = "SCDB_combined_caseCentered.csv"
df_all.to_csv(output_file, index=False)

print("Saved to:", output_file)