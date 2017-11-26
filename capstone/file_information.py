"""
Just a file for all the information on file names, directories and so on.
"""

file_path_data = "./data/"
path_test = "test"
path_train = "train"
text_a = "A"
text_b = "B"
ending = ".txt"
path_filtered = 'filtered_set'

file_path_documentation = "./documentation/"
non_null_frac_name = "non_null_fraction"


def get_data_set_name(test=True, a=True, filtered=False):
    start = path_test if test else path_train
    middle = text_a if a else text_b
    if filtered:
        return path_filtered + ending
    return start + middle + ending


def get_data_set_path(test=True, a=True, filtered=False):
    return file_path_data + get_data_set_name(test, a, filtered)


def get_doc_path(doc_type, test=True, a=True, filtered=False):
    if doc_type == 'frac':
        return file_path_documentation + "fraction_" + get_data_set_name(test, a, filtered)
