import pandas as pd
import numpy as np
import re

# Define constants
NAMES = ['brody', 'saylor', 'ccush', 'shannon', 'heather', 'paul',
         'seb', 'eben', 'peter', 'cam', 'jackson', 'tom', 'lyle',
         'connor', 'john', 'alex', 'calvin', 'mike', 'will']

LOCATIONS = ['bolton', 'chic chocs', 'jay', 'bush', 'ricker', 'tucks',
             'great gulf', 'cochran', 'middlebury', 'whaleback', 'smuggs',
             'tremblant', 'killington', 'baldface', 'notch', 'nosedive','waterville', 'sunday river']

# Compile regex for date pattern
date_pattern = re.compile(r'\b\d{1,2}/\d{1,2}')

# Store parsed data
parsed_data = []

# Open and process each line
with open('data/log.txt', 'r') as f:
    for line in f:
        ski_location = ''
        ski_date = ''
        friends = []

        line = line.lower()
        dates = date_pattern.findall(line)
        if dates:
            ski_date = dates[0]

        words = line.split()
        for word in words:
            if word in LOCATIONS:
                ski_location = word
            if word in NAMES:
                friends.append(word)

        # Store result if there's at least one meaningful entry
        if ski_date or ski_location or friends:
            parsed_data.append({
                'date': ski_date,
                'location': ski_location,
                'friends': ', '.join(friends)
            })

# Convert to DataFrame
df = pd.DataFrame(parsed_data)

# Display or save
print(df.head())
df.to_csv('data/ski_logs.csv', index=False)


