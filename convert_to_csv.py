import pandas as pd
import re

# define constants
NAMES = ['brody', 'saylor', 'ccush', 'shannon', 'heather', 'paul',
         'seb', 'eben', 'peter', 'cam', 'jackson', 'tom', 'lyle',
         'connor', 'john', 'alex', 'calvin', 'mike', 'will', 'robbie']

LOCATIONS = ['bolton', 'chic-chocs', 'jay', 'bush', 'ricker', 'tucks',
             'great gulf', 'cochran', 'middlebury', 'whaleback', 'smuggs',
             'tremblant', 'killington', 'baldface', 'notch', 'nosedive','waterville', 'sunday river']

# Compile regex for date pattern
date_pattern = re.compile(r'\b\d{1,2}/\d{1,2}')

# Store parsed data
parsed_data = []

# Open and process each line
with open('data/log.txt', 'r') as f:
    for line in f:
        ski_location = 'other'
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

        # store result if at least one field is populated
        if ski_date:
            if ski_location != 'other' or friends:
                parsed_data.append({
                    'date': ski_date,
                    'location': ski_location,
                    'friends': ', '.join(friends)
                })

# convert to DF
df = pd.DataFrame(parsed_data)

# convert 'date' to datetime format (assuming year is 2025, add year manually)
df['date'] = pd.to_datetime(df['date'] + '/2025', format='%m/%d/%Y')

# sort by date
df = df.sort_values(by='date')

# save DF
print(df.head())
df.to_csv('data/ski_logs.csv', index=False)



