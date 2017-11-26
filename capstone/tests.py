"""
Contains all tests created throughout the code implementation
"""

import reader
import get_feature_fraction


def test_fraction_read():
    # test with the test set
    df = reader.read_file()
    attr_name_1 = "Row"
    attr_name_2 = "Anon Student Id"
    attr_name_3 = "Step Start Time"
    frac_1 = get_feature_fraction.find_non_null_fraction(df, attr_name_1)
    frac_2 = get_feature_fraction.find_non_null_fraction(df, attr_name_2)
    frac_3 = get_feature_fraction.find_non_null_fraction(df, attr_name_3)
    assert frac_1 == 1.
    assert frac_2 == 1.
    assert frac_3 < 1.

test_fraction_read()
