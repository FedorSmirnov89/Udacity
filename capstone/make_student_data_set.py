"""

Script to create a student centered data set

"""

import pandas as pd
import numpy as np

student_column_name = 'Anon Student Id'
save_path = 'data/averaged_set.txt'


# read the filtered set
df = pd.DataFrame.from_csv('data/filtered_set.txt', sep='\t')
print 'done with the reading'
student_names = pd.unique(df[student_column_name])

row_dict = {}
n_student = 0

# iterate the students
for student in student_names:
    print 'Processing the {} fraction'.format(n_student * 1. / len(student_names))
    n_student += 1
    # take the part describing the student at hand
    df_student = df[df[student_column_name] == student]
    column_dict = {}
    for column in df_student:
        if np.issubdtype(df_student[column].dtype, np.number):
            average = df_student[column].mean()
            if np.isnan(average):
                assert column == 'Error Step Duration (sec)' or column == 'Correct Step Duration (sec)', column
                average = -1
            column_dict[column] = average
    row_dict[student] = column_dict

df_result = pd.DataFrame.from_dict(row_dict, orient='index')
df_result.to_csv(path_or_buf=save_path, sep='\t')
