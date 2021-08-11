import numpy as np
import pandas as pd
import plotly.express as px

def eliminate_row(df, column_to_search, value_to_search):
    """
    INPUTS
    -df: pandas dataframe to modify
    -column_to_search: takes a column name where to search for a specific value
    -value_to_search: takes a value to search in the specified column
    OUPUT
    -returns a dataframe where the unnecessary rows have been eliminated
    """

    #print(column_to_search)
    #print(value_to_search)
    #print(len(df))

    to_drop = []

    for i in range (0, len(df)):
        #print(i)
        #print(to_drop)
        #print(df[column_to_search][i])
        #print(df[column_to_search][i] == value_to_search)
        if df[column_to_search][i] == value_to_search:
            to_drop.append(i)
        else:
            continue
    df = df.drop(to_drop, axis = 0)
    df = df.reset_index(drop = True)
    #print(df)
    #return df.drop(to_drop, axis = 0)
    return df

def make_sub_df(df, columns, row, test_type):
    pta_x = [250, 500, 1000, 2000,
             3000, 4000, 6000, 8000,
             9000, 10000, 11200, 12500,
             14000, 16000, 18000, 20000]
    mtx_x = ["Noise: Left, Speech: Left",
             "Noise: Binaural, Speech: Left",
             "Noise: Binaural, Speech: Binaural",
             "Noise: Binaural, Speech: Right",
             "Noise: Right, Speech: Right"]
    #print(pta_x)
    #print(mtx_x)
    if test_type == "pta":
        x = pta_x
    elif test_type == "mtx":
        x = mtx_x

def drop_130(df, prefix):
    column_names = df.columns
    index_value = df.index[0]
    to_drop = []
    to_search = []
    #print(column_names)
    #print("index = ", index_value)
    #print(len(df))

    for i in column_names:
        #print(i)
        if i.startswith(prefix):
            to_search.append(i)
        else:
            continue
    #print(to_search)

    for j in to_search:
        #print(j)
        #print(df[j])
        #print(df[j][index_value])
        #print(to_drop)
        #print(df[column_to_search][j])
        #print(df[column_to_search][j] == value_to_search)
        if df[j][index_value] == 130:
            #print(True)
            to_drop.append(j)
        else:
            #print(False)
            continue

    print(to_drop)
    print(df)
    df = df.drop(to_drop, axis = 1)
    print(df)
    return df

def plot_pta_L(df):
    """
    INPUTS
    -df: pandas dataframe containing the data to plot
    OUTPUTS
    """

    #print(df)

    df = drop_130(df, "LE_")

    #i = 0
    #data_y = df.loc[i, x_columns]
    #data_y = data_y.reset_index(drop = True)
    #data_y.columns = ["Hearing Threshold (dB HL)"]
    #print(data_y)
    #data_x = pd.DataFrame(data = [250, 500, 1000, 2000, 3000, 4000, 6000, 8000,
    #                              9000, 10000, 11200, 12500, 14000, 16000, 18000, 20000])
    #print(data_x)
    #data = data_x.append(data_y)
    #data.columns = ["Frequency (Hz)", "Hearing Threshold (dB HL)"]
    #print(data)
    #print(data.columns)
    #data.to_csv("../results/data_test.csv")
    #to_drop = []
    #print(data.index)
    #for j in data.index:
        #print(j)
        #print(to_drop)
        #print(data.index[j])
        #print(df[column_to_search][i])
        #print(df[column_to_search][i] == value_to_search)
        #if data[j] == 130:
            #to_drop.append(j)
        #else:
            #continue
    #print(to_drop)
    #data = data.drop(to_drop, axis = 0)
    #print(data)
    #return df.drop(to_drop, axis = 0)
    #ID = df["Participant_ID"][i]
    #name = df["Protocol name"][i]
    #title = ID + "-" + name + " (" + ear + ")"
    #labels = {index: "Frequency (Hz)", value: "Hearing Threshold (dB HL)"}
    #fig = px.line(data, title = title, log_x = True, range_x = [100, 20000], range_y = [-20, 80])
    #fig.show()
    #fig.write_image("../results/" + title + ".png")
