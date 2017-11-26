"""

Script to label all students according to their correctness average

"""

import pandas as pd
import numpy as np

data_path = 'data/averaged_set.txt'
save_path = 'data/benchmark.txt'


# read the average set
df = pd.read_csv(data_path, sep='\t')

students = df['Students']
correctness = df['Corrects']
df_correctness = pd.concat([students, correctness], axis=1)

two_label_column = np.zeros((df_correctness.shape[0], 1))
five_label_column = np.zeros((df_correctness.shape[0], 1))

df_two_labels = pd.DataFrame(two_label_column, columns=['2 Labels'])
df_five_labels = pd.DataFrame(five_label_column, columns=['5 labels'])
df_result = pd.concat([df_correctness, df_two_labels, df_five_labels], axis=1)
df_result = df_result.sort(columns=['Corrects'], ascending=[1])

limit = df_two_labels.shape[0] / 2
df_result.iloc[:limit, 2] = 0
df_result.iloc[limit:, 2] = 1


limit = df_five_labels.shape[0] / 6
df_result.iloc[:limit, 3] = 0
df_result.iloc[limit: 2 * limit, 3] = 1
df_result.iloc[2 * limit: 3 * limit, 3] = 2
df_result.iloc[3 * limit: 4 * limit, 3] = 3
df_result.iloc[4 * limit:, 3] = 4


df_result.to_csv(save_path, sep='\t')




print 'done'