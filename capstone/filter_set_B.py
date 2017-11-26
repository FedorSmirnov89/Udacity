"""
Contains the script to filter entries where features are missing from the training set B, as well as drop all KC-columns
that do not belong to the Rules-KC-model
"""

import pandas as pd

data_folder = 'data/'
set_b = 'trainB.txt'
data_set_path = data_folder + set_b
timing_features_incomplete = ['Step Start Time', 'Step Duration (sec)', 'Correct Transaction Time']
correct_step_name = 'Correct Step Duration (sec)'
incorrect_step_name = 'Error Step Duration (sec)'
kc_rules_name = 'KC(Rules)'
kc_opportunities_name = 'Opportunity(Rules)'
other_kc_names = ['Opportunity(SubSkills)', 'KC(KTracedSkills)', 'Opportunity(KTracedSkills)', 'KC(SubSkills)']

print 'starting data filtering'
# create the data frame
df = pd.DataFrame.from_csv(data_set_path, sep='\t')

# remove entries where one of the timing features is missing
for timing_feature in timing_features_incomplete:
    print 'removing feature {} where missing'.format(timing_feature)
    df = df[df[timing_feature].notnull()]
df = df[df[correct_step_name].notnull() | df[incorrect_step_name].notnull()]

# remove the entries where the KC is not Rules
df = df[df[kc_rules_name].notnull()]
assert df[df[kc_opportunities_name].isnull()].size == 0

# drop the entries of the other kc models
for drop_column in other_kc_names:
    df.drop(drop_column, axis=1, inplace=True)

save_path = data_folder + 'filtered_set.txt'
df.to_csv(save_path, sep='\t')
print 'data filtering done'
