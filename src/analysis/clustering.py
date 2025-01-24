import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Step 1: Merge order_items with users to get the necessary information
order_items =  pd.read_csv('../../data/processed/cleaned_order_items.csv')
users = pd.read_csv('../../data/processed/cleaned_users.csv') 

order_items_with_users = order_items.merge(users, left_on='user_id', right_on='id', how='left')

# Step 2: Calculate total spending and total products bought by each user
user_spending = order_items_with_users.groupby('user_id')['sale_price'].sum().reset_index()
user_product_count = order_items_with_users.groupby('user_id')['product_id'].count().reset_index()

# Merge the two dataframes to have both spending and product count for each user
user_data = pd.merge(user_spending, user_product_count, on='user_id')
user_data.columns = ['user_id', 'total_spent', 'total_products_bought']

print(user_data)
user_data.to_csv('user_data_with_clusters.csv', index=False)

# Step 3: Standardize the data (important for K-Means)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(user_data[['total_spent', 'total_products_bought']])

# Step 4: Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # You can adjust n_clusters
user_data['cluster'] = kmeans.fit_predict(scaled_data)

# Step 5: Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(user_data['total_spent'], user_data['total_products_bought'], c=user_data['cluster'], cmap='viridis')
plt.xlabel('Total Spending')
plt.ylabel('Total Products Bought')
plt.title('Clustering of Users Based on Spending and Products Bought')
plt.colorbar(label='Cluster')
plt.show()

# Step 6: Show the clustered data
#print(user_data.head())
# Calculate the number of users per cluster
users_per_cluster = user_data['cluster'].value_counts().sort_index()

# Print the number of users per cluster
print("Number of users per cluster:")
print(users_per_cluster)


# Step 1: Merge order_items with users to get the necessary information
order_items =  pd.read_csv('../../data/processed/cleaned_order_items.csv')
users = pd.read_csv('../../data/processed/cleaned_users.csv') 

order_items_with_users = order_items.merge(users, left_on='user_id', right_on='id', how='left')

# Step 2: Calculate total spending and total products bought by each user
user_spending = order_items_with_users.groupby('user_id')['sale_price'].sum().reset_index()
user_product_count = order_items_with_users.groupby('user_id')['product_id'].count().reset_index()

# Merge the two dataframes to have both spending and product count for each user
user_data = pd.merge(user_spending, user_product_count, on='user_id')
user_data.columns = ['user_id', 'total_spent', 'total_products_bought']

# Step 3: Standardize the data (important for K-Means)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(user_data[['total_spent', 'total_products_bought']])

# Step 4: Elbow Method to find the best number of clusters
inertia = []
silhouette_scores = []
K_range = range(2, 11)  # Trying 2 to 10 clusters

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)
    
    # Calculate silhouette score for each k
    score = silhouette_score(scaled_data, kmeans.labels_)
    silhouette_scores.append(score)

# Step 5: Plot Elbow Method
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(K_range, inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')

# Step 6: Plot Silhouette Scores
plt.subplot(1, 2, 2)
plt.plot(K_range, silhouette_scores, marker='o', color='green')
plt.title('Silhouette Scores')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')

plt.tight_layout()
plt.show()

# Step 7: Find the optimal number of clusters
optimal_k_elbow = K_range[inertia.index(min(inertia))]
optimal_k_silhouette = K_range[silhouette_scores.index(max(silhouette_scores))]

print(f"Optimal number of clusters (Elbow Method): {optimal_k_elbow}")
print(f"Optimal number of clusters (Silhouette Score): {optimal_k_silhouette}")