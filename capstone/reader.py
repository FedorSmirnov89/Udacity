"""

File containing methods to read the files and provide the pandas data frames containing the information

"""

import pandas as pd
import file_information


chunk_size = 1000000


def read_file(test=True, a=True, filtered=False):
    """
    Read the specified file and return the created data frame
    :param test: TRUE - test; False - train
    :param a: TRUE - a; False - b
    :return: Data frame containing the specified information or the reader if the file is too big
    """
    path_first = file_information.path_test if test else file_information.path_train
    path_second = file_information.text_a if a else file_information.text_b
    path = file_information.file_path_data + path_first + path_second + file_information.ending
    if filtered:
        path = file_information.file_path_data + file_information.path_filtered + file_information.ending

    if not test and a:
        reader = pd.read_csv(path, sep='\t', chunksize=chunk_size)
        return reader
    else:
        result = pd.read_csv(path, sep="\t")
        return result
