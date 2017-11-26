"""

In this file, I want to have the preprocessing of the set

"""

import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import normaltest
import numpy as np


input_path = 'data/averaged_set.txt'
str_step = 'Step Duration (sec)'
str_correct = 'Correct Step Duration (sec)'
str_incorrect = 'Error Step Duration (sec)'
time_labels = [str_step, str_correct, str_incorrect]

df = pd.DataFrame.from_csv(input_path, sep='\t')
corr = df.corr()
plt.matshow(corr)
plt.xticks(range(len(df.columns)), df.columns, rotation='vertical')
plt.yticks(range(len(df.columns)), df.columns)
plt.show()


# check for the ch squared value
for feature in df:
    (chi_sq, p_norm) = normaltest(df[feature])
    print '{} has a chi squared of {:4.4f} and a p norm value of {:4.4f}'.format(feature, chi_sq, p_norm)

# replace the zeros by a small value
df[df == 0] = .00001
df[df < 0] = .00001
print ''


# perform a logarithmic transformation
log_df = np.log(df)
# check for the ch squared value
for feature in log_df:
    (chi_sq, p_norm) = normaltest(log_df[feature])
    print '{} has a chi squared of {:4.4f} and a p norm value of {:4.4f}'.format(feature, chi_sq, p_norm)

