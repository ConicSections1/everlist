import os
from datetime import datetime

# Directory to scan
directory = '.'

# Output file
output_file = 'everlist.txt'

# Load existing entries from file
existing_entries = {}

if os.path.exists(output_file):
    with open(output_file, 'r') as f:
        for line in f:
            parts = line.strip().split(' - first seen on ')
            if len(parts) == 2:
                existing_entries[parts[0]] = parts[1]

# Scan current directory for new entries
current_entries = os.listdir(directory)

for entry in current_entries:
    if entry == output_file:
        continue
    if entry not in existing_entries:
        first_seen = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        existing_entries[entry] = first_seen

# Write updated list back to file, sorted alphabetically
with open(output_file, 'w') as f:
    for entry in sorted(existing_entries.keys()):
        f.write(f"{entry} - first seen on {existing_entries[entry]}\n")

print(f"File list updated in '{output_file}'")
