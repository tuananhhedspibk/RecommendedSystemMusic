import pandas as pd
from scipy.spatial.distance import cosine

if __name__ == "__main__":
	data = pd.read_csv("data.csv")
	print data.shape
	print data.head(8).ix[:, 0:6]	# data for first 8 lines, first 6 columns

# --- Start Item Based Recommendations ---
# Drop any column named "user"
# Based on artist data, we will recommended similar artist for user
# so we don't need data of user here
data_item_base = data.drop("user", 1)

# We will create square matrix for same measure
# This square matrix describe about similar between items-items
# artists - artists

data_item_base_frame = pd.DataFrame(index = data_item_base.columns, 
	columns=data_item_base.columns)

print data_item_base_frame.head(6).ix[:, 0:6]

# Calculate similarily
# for i in range(0, len(data_item_base_frame.columns)):
# 	for j in range(0, len(data_item_base_frame.columns)):
# 		data_item_base_frame.ix[i, j] = 1 - cosine(data.ix[:, i], data.ix[:, j])

#data_item_base_frame.to_csv("data_item_base_frame.csv", sep=",", encoding="utf-8")

data_item_base_frame = pd.read_csv("data_item_base_frame.csv")
print data_item_base_frame.head(6).ix[:,0:5]

data_neighbors = pd.DataFrame(index=data_item_base_frame.columns, columns = range(1, 11))

for i in range(0, len(data_item_base_frame.columns)):
	data_neighbors.ix[i, :10] = data_item_base_frame.ix[0:, i].sort_values(ascending=False)[:10].index

print data_neighbors.head(6).ix[:,0:4]