"""
Script to test the robustness of the classifier

"""


import pandas as pd
import numpy as np

from sklearn.cluster import KMeans


test_bench_path = 'data/test_bench.txt'
test_data_path = 'data/test_data.txt'
train_data_path = 'data/train_data.txt'


# read the dfs
df_test_bench = pd.read_csv(test_bench_path, sep='\t').sort(columns=['Row'], ascending=[1])
df_train_data = pd.read_csv(train_data_path, sep='\t').sort(columns=['Row'], ascending=[1])
df_test_data = pd.read_csv(test_data_path, sep='\t').sort(columns=['Row'], ascending=[1])


clusterer = KMeans(n_clusters=2, random_state=1)

# train the clusterer with the train data
cp_1 = df_train_data['PC 1']
cp_2 = df_train_data['PC 2']

X_train = pd.concat([cp_1, cp_2], axis=1)
clusterer.fit(X_train)

cp_1_test = df_test_data['PC 1']
cp_2_test = df_test_data['PC 2']
X_test = pd.concat([cp_1_test, cp_2_test], axis=1)
preds = clusterer.predict(X_test)

ser_preds = pd.Series(preds)

bench = df_test_bench['2 Labels']
res_bench = bench.reset_index()['2 Labels']
df_compare = pd.concat([ser_preds, res_bench], axis=1)

# find out whether there are more 1s or 0s in the prediction
v_count = ser_preds.value_counts()
n_ones = v_count[1]
n_zeros = v_count[0]
if n_zeros > n_ones:
    predicted_good = 1
    predicted_bad = 0
else:
    predicted_good = 0
    predicted_bad = 1

# bench = 0 => low performance
# pred = 0 => high performance
# results with respect to high performance
n_students = df_test_data.shape[0]
n_same_result = df_compare[(df_compare['2 Labels'] == 1) & (df_compare.iloc[:, 0] == 0)].shape[0]
true_positive_ratio = df_compare[(df_compare['2 Labels'] == 1) & (df_compare.iloc[:, 0] == predicted_good)].shape[0] \
                      * 1. / n_students
true_negative_ratio = df_compare[(df_compare['2 Labels'] == 0) & (df_compare.iloc[:, 0] == predicted_bad)].shape[0] \
                      * 1. / n_students
false_positive_ratio = df_compare[(df_compare['2 Labels'] == 1) & (df_compare.iloc[:, 0] == predicted_bad)].shape[0] \
                      * 1. / n_students
false_negative_ratio = df_compare[(df_compare['2 Labels'] == 0) & (df_compare.iloc[:, 0] == predicted_good)].shape[0] \
                      * 1. / n_students

print 'The {} with respect to the benchmark is {}'.format('true_positive_ratio', true_positive_ratio)
print 'The {} with respect to the benchmark is {}'.format('true_negative_ratio', true_negative_ratio)
print 'The {} with respect to the benchmark is {}'.format('false_positive_ratio', false_positive_ratio)
print 'The {} with respect to the benchmark is {}'.format('false_negative_ratio', false_negative_ratio)
print 'The ratio of students predicted as good is {}'.format(df_compare[df_compare.iloc[:, 0] == predicted_good].shape[0]
                                                             * 1. / n_students)
print ''
print ''
