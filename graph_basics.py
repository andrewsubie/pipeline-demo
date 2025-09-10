import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('data/ski_logs.csv')

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# # === 1. Ski Days Over Time ===
# df['week'] = df['date'].dt.to_period('W').apply(lambda r: r.start_time)
# weekly_counts = df.groupby('week').size()
#
# plt.figure(figsize=(10, 5))
# weekly_counts.plot(kind='line', marker='o')
# plt.title('Ski Days Over Time')
# plt.xlabel('Week')
# plt.ylabel('Number of Ski Days')
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('graphs/ski_days_over_time.png')
# plt.show()

# === 2. Top Locations ===
location_counts = df['location'].value_counts().head(10)

plt.figure(figsize=(8, 5))
location_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 Ski Locations')
plt.xlabel('Location')
plt.ylabel('Number of Visits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('graphs/top_locations.png')
plt.show()

# === 3. Top Friends ===
# Split friends column and count all names
friend_series = df['friends'].dropna().str.split(', ')
all_friends = friend_series.explode()
friend_counts = all_friends.value_counts().head(10)

plt.figure(figsize=(8, 5))
friend_counts.plot(kind='bar', color='lightgreen')
plt.title('Top 10 Ski Friends')
plt.xlabel('Friend')
plt.ylabel('Number of Ski Days Together')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('graphs/top_friends.png')
plt.show()
