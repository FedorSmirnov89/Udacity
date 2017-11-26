"""
Script to get the number of problem steps solved by each student

"""

import pandas as pd
import numpy as np

student_column_name = 'Anon Student Id'
file_path = 'documentation/student_step_ratio.txt'


# get the df of the filtered data set
df_filtered = pd.DataFrame.from_csv('data/filtered_set.txt', sep='\t')
# get the student column
ser_student = df_filtered[student_column_name]
# only keep the unique stuff
ser_student_unique = pd.unique(ser_student)

str_result = ''
str_result += "Overall, there are {} students in the filtered data set".format(ser_student_unique.size)

print str_result

# create a data frame where each student points to the number of problem steps he/she solved
problem_step_numbers = []
student_num = 0
for student in ser_student_unique:
    student_num += 1
    problem_step_numbers.append(df_filtered[df_filtered[student_column_name] == student].shape[0])
    if student_num % 10 == 0:
        print 'Done with {} percent of the students'.format(student_num / 3269. * 100)

np_a = np.array(problem_step_numbers)

str_stats = 'Maximal: {}; Minimum: {}; Average: {}; Deviation:{}'.format(np.max(np_a), np.min(np_a),
                                                                         np.average(np_a), np.std(np_a))
print str_stats
str_result += '\n' + str_stats

save_file = open(file_path, 'w')
save_file.write(str_result)
save_file.close()
