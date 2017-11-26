"""

Perform a min- max- scaling for the averaged set

"""
import pandas as pd
import numpy as np
from sklearn import preprocessing


data_path = 'data/averaged_set.txt'
save_path = 'data/rescaled_set.txt'
save_path_2 = 'data/rescaled2_set.txt'

# read the averaged set
df_average = pd.read_csv(data_path, sep='\t')
df_average_2 = pd.DataFrame.from_csv(data_path, sep='\t')

# find the min and the max for each column
extremes = {}
for column in df_average:
    if np.issubdtype(df_average[column].dtype, np.number):
        maximum = df_average[column].max()
        minimum = df_average[column].min()
        extremes[column] = (maximum, minimum)

# create a dict for a rescaled data frame
rescaled_dict = {}
for idx, row in df_average.iterrows():
    print 'Processing the {} fraction'.format(1. * idx / df_average.shape[0])
    name = row['Students']
    rescaled_dict[name] = {}
    for column in df_average:
        if column != 'Students':
            maximum = extremes[column][0]
            minimum = extremes[column][1]
            unscaled = row[column]
            value = 1. * (unscaled - minimum) / (maximum - minimum)
            assert not np.isnan(value)
            rescaled_dict[name][column] = value

df_result = pd.DataFrame.from_dict(rescaled_dict, orient='index')
scaled = preprocessing.scale(df_average_2)
df_scaled = pd.DataFrame(data=scaled, columns=df_average_2.columns, index=df_average_2.index)
df_result.to_csv(save_path, sep='\t')
df_scaled.to_csv(save_path_2, sep='\t')

