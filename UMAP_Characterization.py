## PACKAGES:
import pandas as pd
import numpy as np
import os
import matplotlib
import umap.umap_ as umap
import plotly.express as px
import random
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from yellowbrick.cluster import SilhouetteVisualizer

## DATASET:
df = pd.read_csv('SimulationMCIsCoimbra.csv')
print(df)
print(df.columns)

## PRE-PROCESSING:

#Step 1: Transformations and cleaning.
#Transforming categorical data to numeric of binary.
df = pd.get_dummies(df, drop_first=True)
#Replacing missing values with a dummy variable arbitrarily such as -4.
df.fillna(-4, inplace=True)
#Confirming that there are no remaining missing values.
print(df.isnull().sum())

#Excluding columns that may not be of interest for the analysis.
exclude_columns = ['RID', 'MONTH', 'YEAR']
df_filtered = df.drop(columns=exclude_columns)

#Step 2: Scaling.
#Standardizing variables with the greatest dispersion.
dispersion = df_filtered.select_dtypes(include=['float64', 'int64']).std()
print("Standard deviation of numeric columns:\n", dispersion)

top_dispersion_columns = dispersion.nlargest(10).index #In this case, 10 variables were highly dispersed.
print("Columns with greatest dispersion:", top_dispersion_columns)

df_scaled = df_filtered.copy()
scaler = StandardScaler()
df_scaled[top_dispersion_columns] = scaler.fit_transform(df_scaled[top_dispersion_columns])

#Comparing the changes may be of interest, therefore:  
print("Original Dataframe:\n", df_filtered)
print("Scaled Dataframe:\n", df_scaled)

## DIMENSION REDUCTION (UMAP):

features = df_scaled.loc[:, :'MHSTROKE_Present']

np.random.seed(123)
umap_2d = umap.UMAP(n_components=2, init='random', random_state=0)
proj_2d = umap_2d.fit_transform(features)

#Choosing one of the variables ('EDUCAT') to check the clustering configuration. 
fig_2d = px.scatter(
    proj_2d, x=0, y=1, 
    color=df_scaled.EDUCAT, labels={'color': 'EDUCAT'}
)
fig_2d.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
fig_2d.show()

#LABELING-AREAS ('cluster_info'):

#Designing the areas of each cluster (xmin, ymin, xmax, ymax):
cluster1_coords = (1, -8, 7.5, 0) #In this example we obtained two clusters.
cluster2_coords = (5, 8, 11, 16)
df_scaled_without_cluster = df_scaled
clusters_areas = [cluster1_coords, cluster2_coords]

bbox_indices = np.full(proj_2d.shape[0], -1)

#Checking each point against each bounding box.
for idx, bbox in enumerate(clusters_areas):
    xmin, ymin, xmax, ymax = bbox
    inside_bbox = (proj_2d[:, 0] >= xmin) & (proj_2d[:, 0] <= xmax) & (proj_2d[:, 1] >= ymin) & (proj_2d[:, 1] <= ymax)
    bbox_indices[inside_bbox] = idx

#Combining the original points and the bounding box index into a new array.
points_with_bbox_info = np.column_stack((proj_2d, bbox_indices))
bbox_info_df = pd.DataFrame(points_with_bbox_info, columns=['umap_x', 'umap_y', 'cluster_info'])

#Adding the bounding box information to the original dataframe.
df_scaled_with_clusters2 = pd.concat([df_scaled_without_cluster, bbox_info_df], axis=1)
print("DataFrame with clusters:")
print(df_scaled_with_clusters2)

#ASSESSING EACH VARIABLE:

#Characterizing the clusters according to the variables available (w/ count):
df_scaled_with_clusters2['UMAP_1'] = proj_2d[:, 0]
df_scaled_with_clusters2['UMAP_2'] = proj_2d[:, 1]
#Iterating over each variable in features.
for variable in features.columns:
    if variable in ['UMAP_1', 'UMAP_2']:
        continue  # Skip UMAP projections themselves

    #Filtering out rows with dummy values (-4).
    df_scaled_filtered = df_scaled_with_clusters2[df_scaled_with_clusters2[variable] != -4]

    #Creating scatter plot with marginal histograms.
    fig = px.scatter(
        df_scaled_with_clusters2, x='UMAP_1', y='UMAP_2', color=variable,
        labels={'color': variable}
    )
    fig.show()
    # Computing and visualize statistics (value counts) per cluster_info
    value_counts = df_scaled_filtered.groupby('cluster_info')[variable].value_counts().unstack(fill_value=0)
    print(f"Value Counts for {variable}:")
    print(value_counts)

#FOCUSING ON FLUID BIOMARKERS INFORMATION:

#Obtaining information (count) for percentage calculation related to normal/abnormal biomarkers (amyloid, tauopathy, and neurodegeneration) by cluster: 
value_counts_clusters = df_scaled_with_clusters2['cluster_info'].value_counts()
print(value_counts_clusters)

value_counts_AMYLOID = df_scaled_with_clusters2.groupby('cluster_info')['AMYLOID'].value_counts().unstack(fill_value=0)
value_counts_TAUTOPA = df_scaled_with_clusters2.groupby('cluster_info')['TAUTOPA'].value_counts().unstack(fill_value=0)
value_counts_NEURODEG = df_scaled_with_clusters2.groupby('cluster_info')['NEURODEG'].value_counts().unstack(fill_value=0)

print(value_counts_AMYLOID)
print()
print(value_counts_TAUTOPA)
print()
print(value_counts_NEURODEG)

#Generating the AT(N) scheme:
df_scaled_with_clusters2['ATN'] = df_scaled_with_clusters2[['AMYLOID', 'TAUTOPA', 'NEURODEG']].astype(str).agg(''.join, axis=1)
value_counts_ATN = df_scaled_with_clusters2.groupby('cluster_info')['ATN'].value_counts().unstack(fill_value=0)
print(value_counts_ATN)
print()

## PARTITION CLUSTERING (K-MEANS) AND SILHOUETTE SCORES:

km = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init='auto', random_state=0) #In this example we obtained two clusters.
kmeans_labels= km.fit_predict(df_scaled)

#Calculating the average Silhouette coefficient.
score = silhouette_score(df_scaled, km.labels_, metric='euclidean')
print('Silhouetter Score: %.4f' % score) 

#Silhouette plot.
visualizer = SilhouetteVisualizer(km)
visualizer.fit(df_scaled)
