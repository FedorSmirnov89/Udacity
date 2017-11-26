
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from sklearn.mixture import GMM
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import Birch


clusterers = [GMM(n_components=2), DBSCAN(eps=.1), KMeans(n_clusters=2), SpectralClustering(n_clusters=2),
              AgglomerativeClustering(n_clusters=2), Birch(n_clusters=2, threshold=.0625)]

color_map = {0: 'b', 1: 'r', 2: 'g', 3: 'k', 4: 'c', 5: 'm', 6: 'y', 7: 'w', -1: 'w'}

data_path = 'data/two_principal_components.txt'

df_data = pd.read_csv(data_path, sep='\t')
for clusterer in clusterers:
    pc_1 = df_data['PC 1']
    pc_2 = df_data['PC 2']
    df_input = pd.concat([pc_1, pc_2], axis=1)
    preds = clusterer.fit_predict(df_input)
    color = [color_map[l] for l in preds]
    plt.scatter(pc_1, pc_2, color=color)
    plt.ylabel('PC 2')
    plt.xlabel('PC 1')
    preds = np.array(preds)
    ratio = preds[preds == 1].shape[0] * 1. / preds.shape[0]
    plt.title('Clustering using {}, ratio of {}'.format(type(clusterer).__name__, ratio))
    plt.show()
