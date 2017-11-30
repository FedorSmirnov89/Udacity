"""
Script for the creation of the data used for the robustness set.

"""

import pandas as pd
import numpy as np

data_path = 'data/two_principal_components.txt'
benchmark_path = 'data/benchmark2.txt'

test_bench_path = 'data/test_bench.txt'
test_data_path = 'data/test_data.txt'
train_data_path = 'data/train_data.txt'
test_set_size = 320

# read in the benchmark and the pc data
df_data = pd.read_csv(data_path, sep='\t')
df_bench = pd.read_csv(benchmark_path, sep='\t')
df_bench = df_bench.sort(columns=['Row'], ascending=[1])

# extract x random individuals from both sets and create data frames that consist of the remaining data
access_array = np.random.randint(df_bench.shape[0], size=(test_set_size,))
remain_array = df_bench.index.isin(access_array)
df_test_bench = df_bench.iloc[access_array]
df_test_data = df_data.iloc[access_array]
df_train_data = df_data[~remain_array]

# save the four new files
df_test_bench.to_csv(test_bench_path, sep='\t')
df_test_data.to_csv(test_data_path, sep='\t')
df_train_data.to_csv(train_data_path, sep='\t')

print 'all done'
