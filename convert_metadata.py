import re

# Define file paths
input_file = "/home/arindam/indic-hindi-english-dataset/txt.done.data"  # Adjust path if needed
output_file = "/home/arindam/indic-hindi-english-dataset/metadata.csv"

# Read input file
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Process lines and extract (ID | text)
data = []
for line in lines:
    match = re.match(r"\(\s*(\S+)\s+\"(.*)\"\s*\)", line)
    if match:
        file_id, text = match.groups()
        data.append(f"{file_id}|{text}")

# Write to metadata.csv
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(data))

print(f"✅ Converted metadata saved at: {output_file}")
