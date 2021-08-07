import numpy as np
import pandas as pd

def eliminate_row(df, column_to_search, value_to_search):
    """
    INPUTS
    -df: pandas dataframe to modify
    -column_to_search: takes a column name where to search for a specific value
    -value_to_search: takes a value to search in the specified column
    OUPUT
    -returns a dataframe where the unnecessary rows have been eliminated
    """

    print(column_to_search)
    print(value_to_search)
    print(len(df))
    to_drop = []

    for i in range (0, len(df)):
        #print(i)
        #print(to_drop)
        #print(df[column_to_search][i])
        print(df[column_to_search][i] == value_to_search)
        if df[column_to_search][i] == value_to_search:
            to_drop.append(i)
        else:
            continue
    df = df.drop(to_drop, axis = 0)
    #print(df)
    #return df.drop(to_drop, axis = 0)
    return df
