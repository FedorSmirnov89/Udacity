"""
Contains methods for the data analysis and preprocessing that is done before the application of any learning algos
"""
import reader
import file_information
import pandas as pd


def find_non_null_fraction(df, attr_name):
    """
    Return the fraction of set attributes.

    :param df: The analyzed data frame
    :param attr_name: The attribute name to look at
    :return: (double) fraction of the entries where the given attribute is not null
    """

    # get the right attribute column
    ser = df[attr_name]
    n_entries = ser.size
    n_non_null = ser[ser.notnull()].size
    result = 1. * n_non_null / n_entries
    return result


def create_fraction_map(df):
    """
    Goes through the attributes (rows) of the given data frame and calculates the non null fraction for each of them
    The result is a dict containing the result
    :param df: (DataFrame) the given data frame
    :return: (dict) dictionary - attribute name : non null fraction
    """

    result = {}
    for attr_name in list(df):
        fraction = find_non_null_fraction(df, attr_name)
        result[attr_name] = fraction
    return result


def make_frac_file(test=True, a=True):
    """
    Create the fraction maps for the specified data set and print it into a log file
    :param test:
    :param a:
    :return:
    """

    if not test and a:
        # work in chunks
        dic = {}
        n_chunks = 0
        for chunk in reader.read_file(test=test, a=a):
            n_chunks += 1
            print "Current chunk number - {}".format(n_chunks)
            for attr_name in list(chunk):
                if not attr_name in dic:
                    dic[attr_name] = find_non_null_fraction(chunk, attr_name)
                else:
                    dic[attr_name] += find_non_null_fraction(chunk, attr_name)
        for key, value in dic.iteritems():
            dic[key] = value / n_chunks
    else:
        df = reader.read_file(test, a)
        dic = create_fraction_map(df)

    doc_path = file_information.get_doc_path("frac", test, a)
    file_ = open(doc_path, "w")
    for attr_name, fraction in dic.iteritems():
        line = "{} : {} \n".format(attr_name, fraction)
        file_.write(line)
    file_.close()
