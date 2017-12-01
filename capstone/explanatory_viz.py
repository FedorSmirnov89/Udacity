"""

Script to create the explanatory visualization plot

"""

import pandas as pd
from matplotlib import pyplot as plt

from sklearn.cluster import KMeans


data_path = 'data/two_principal_components.txt'
color_map = {0: 'b', 1: 'r'}

# read the data
df = pd.read_csv(data_path, sep='\t')
# train algo and make predictions
clusterer = KMeans(n_clusters=2, random_state=1)
pc_1 = df['PC 1']
pc_2 = df['PC 2']
df_input = pd.concat([pc_1, pc_2], axis=1)
preds = clusterer.fit_predict(df_input)
color = [color_map[l] for l in preds]
df_input['prediction'] = preds
df_gifted = df_input[df_input['prediction'] == 0]
df_less_skilled = df_input[df_input['prediction'] == 1]

min_pc1 = df_gifted['PC 1'].min(axis=0)
max_pc1 = df_less_skilled['PC 1'].max(axis=0)
max_pc1_gifted = df_gifted['PC 1'].max(axis=0)

min_pc2 = df_less_skilled['PC 2'].min(axis=0)
max_pc2 = df_less_skilled['PC 2'].max(axis=0)
max_pc2_gifted = df_gifted['PC 2'].max(axis=0)

cb1 = (max_pc1_gifted - min_pc1) / (max_pc1 - min_pc1)
cb2 = (max_pc2_gifted - min_pc2) / (max_pc2 - min_pc2)
print 'classification border pc1:{}, classification border pc2:{}'.format(cb1, cb2)

plt.scatter(pc_1, pc_2, color=color)
plt.axvline(x=max_pc1_gifted, color='k')
plt.axvline(x=max_pc1, color='k', linestyle='--')
plt.axvline(x=min_pc1, color='k', linestyle='--')
plt.axhline(y=max_pc2_gifted, color='k')
plt.axhline(y=max_pc2, color='k', linestyle='--')
plt.axhline(y=min_pc2, color='k', linestyle='--')
plt.axhline(y=max_pc2_gifted, color='k')
plt.xticks([min_pc1, max_pc1_gifted, max_pc1], (0, '{:10.2f}'.format(cb1 * 100), 100))
plt.yticks([min_pc2, max_pc2_gifted, max_pc2], (0, '{:10.2f}'.format(cb2 * 100), 100))
plt.xlabel('Relative incorrectness [%]')
plt.ylabel('Relative slowness [%]')
plt.show()