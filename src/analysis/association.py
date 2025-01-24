import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules

# Load the data
order_items = pd.read_csv('../../data/processed/cleaned_order_items.csv')
products = pd.read_csv('../../data/processed/cleaned_products.csv')

# Merge to include brand information
merged = pd.merge(order_items, products[['id', 'brand']], left_on='product_id', right_on='id')

# Group by user_id to create transaction lists by brand
transactions_by_user = merged.groupby('user_id')['brand'].apply(set).reset_index()
transactions_by_user['brand'] = transactions_by_user['brand'].apply(list)

# Convert to one-hot encoded sparse matrix
brands = sorted(set(merged['brand']))
ohe_data = pd.DataFrame(0, index=transactions_by_user['user_id'], columns=brands)

for idx, row in transactions_by_user.iterrows():
    ohe_data.loc[row['user_id'], row['brand']] = 1

# Run FP-Growth
min_support = 0.001  # Adjust as needed
frequent_itemsets = fpgrowth(ohe_data, min_support=min_support, use_colnames=True)

# Generate Association Rules
num_itemsets = 10  # Adjust based on how many itemsets you want
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0, num_itemsets=num_itemsets)

# Output results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules)

import matplotlib.pyplot as plt

# Filter out itemsets with only one item
frequent_itemsets_filtered = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x) > 1)]

# Sort the filtered frequent itemsets by support value
frequent_itemsets_sorted = frequent_itemsets_filtered.sort_values(by='support', ascending=False)

# Select top 10 frequent itemsets
top_itemsets = frequent_itemsets_sorted.head(10)

# Plot
plt.figure(figsize=(10,6))
plt.bar(top_itemsets['itemsets'].astype(str), top_itemsets['support'], color='skyblue')
plt.xlabel('Itemsets')
plt.ylabel('Support')
plt.title('Top 10 Frequent Itemsets by Brand (Filtered)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()