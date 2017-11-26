"""

Apply PCA to transform the features we have down to 2 (for visualization reasons)

"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


data_path = 'data/rescaled_set.txt'
save_path = 'data/two_principal_components.txt'

# read the data
df = pd.read_csv(data_path, sep='\t')

# save the students column
students = df[df.columns[0]]
df = df.drop(df.columns[0], axis=1)


# perform the pca
pca = PCA(n_components=2)
pca.fit(df)

# plot the distribution of the components on the original features
components = pca.components_
first = components[0]
plt.bar(range(8), first)
plt.title('Distribution first PC')
plt.ylabel('Weights')
plt.xlabel('Features')
plt.xticks(np.arange(8) + .5, df.columns)
plt.show()

second = components[1]
plt.bar(range(8), second)
plt.title('Distribution second PC')
plt.ylabel('Weights')
plt.xlabel('Features')
plt.xticks(np.arange(8) + .5, df.columns)
plt.show()



expl_var = pca.explained_variance_ratio_
sum_var = 0
for i in range(0, 2):
    print "Principal component number {} has an explained variance of {}".format(i + 1, expl_var[i])
    sum_var += expl_var[i]
    print "The sum of the first {} components is {}".format(i+1, sum_var)

transformed = pca.transform(df)


# concatenate it with the student column
df_transformed = pd.DataFrame(transformed, columns=['PC 1', 'PC 2'])
df_result = pd.concat([students, df_transformed], axis=1)
df_result = df_result.rename(columns={df_result.columns[0]: 'Student name'})

df_result.to_csv(save_path, sep='\t')
