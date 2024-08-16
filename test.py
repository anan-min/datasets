import pandas as pd

# Load the CSV file
df = pd.read_csv('reviews_0-250.csv', low_memory=False)


# Determine the number of rows
num_rows = len(df)  # Should be 251 rows for 0-250 range

# Calculate the split points
split_size = num_rows // 5  # Integer division to find the size of each part
split_points = [split_size * i for i in range(1, 5)]


# Split the DataFrame into five parts
df_part1 = df.iloc[:split_points[0]]              # Rows 0 to 50
df_part2 = df.iloc[split_points[0]:split_points[1]]  # Rows 51 to 100
df_part3 = df.iloc[split_points[1]:split_points[2]]  # Rows 101 to 150
df_part4 = df.iloc[split_points[2]:split_points[3]]  # Rows 151 to 200
df_part5 = df.iloc[split_points[3]:]              # Rows 201 to 250



# Save each part
df_part1.to_csv('reviews_0-50.csv', index=False)
df_part2.to_csv('reviews_51-100.csv', index=False)
df_part3.to_csv('reviews_101-150.csv', index=False)
df_part4.to_csv('reviews_151-200.csv', index=False)
df_part5.to_csv('reviews_201-250.csv', index=False)


print("done")