"""

Script to make a scatter plot of the two principal components

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.mixture import GMM
from sklearn.metrics import silhouette_score
from sklearn import preprocessing


data_path = 'data/two_principal_components.txt'
data_path_bench = 'data/benchmark2.txt'

# read the df
df = pd.DataFrame.from_csv(data_path, sep='\t')
pc_1 = df['PC 1']
pc_2 = df['PC 2']
df_data_only = pd.concat([pc_1, pc_2], axis=1)
scaled_input = preprocessing.scale(df_data_only)

color_map = {0: 'b', 1: 'r', 2: 'g', 3: 'k', 4: 'c'}
marker_map = {0: 'o', 1: 'x', 2: '*', 3: 'v', 4: 'h'}

# get the benchmark for comparison
df_bench = pd.read_csv(data_path_bench, sep='\t')
df_bench = df_bench.sort(columns=['Row'], ascending=[1])
bench_two = df_bench['2 Labels'].values
bench_five = df_bench['5 labels'].values

scores = []
# try different numbers of clusters
for n_clusters in range(2, 6):
    clusterer = GMM(n_components=n_clusters, random_state=1)
    clusterer.fit(scaled_input)
    preds = clusterer.predict(df_data_only)
    score = silhouette_score(df_data_only, preds)
    color = [color_map[l] for l in preds]
    plt.scatter(preprocessing.scale(pc_1), preprocessing.scale(pc_2), color=color)
    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    plt.title('Clustering with {} clusters'.format(n_clusters))
    plt.show()
    scores.append(score)

# plot all the data
# plot the benchmark visualization
plt.scatter(pc_1, pc_2)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.title('Shape of the data')
plt.show()

# plot the benchmark visualization
color = [color_map[l] for l in bench_two]
plt.scatter(pc_1, pc_2, color=color)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.title('Benchmark 2 Groups')
plt.show()

color = [color_map[l] for l in bench_five]
plt.scatter(pc_1, pc_2, color=color)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.title('Benchmark 5 Groups')
plt.show()


# plot the scores based on the number of clusters
plt.plot(range(2, 6), scores)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.show()
