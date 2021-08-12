import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

"""
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
"""

def return_130(df, to_search):
    index_value = df.index[0]
    to_drop = []
    #print(column_names)
    #print("index = ", index_value)
    #print(len(df))

    for i in to_search:
        #print(i)
        #print(df[i])
        #print(df[i][index_value])
        #print(to_drop)
        #print(df[column_to_search][i])
        #print(df[column_to_search][i] == value_to_search)
        if df[i][index_value] == 130:
            #print(True)
            to_drop.append(to_search.index(i))
        else:
            #print(False)
            continue

    #print(to_drop)
    #print(df)
    #to_search_int = to_search_int.drop(to_drop, axis = 1)
    return to_drop

#def drop_130(data, list_130):
    #for j in list_130:
        #print(.columns[j])
        #df = df.drop(df.columns(j), axis = 1)

def plot_pta_L(df):
    """
    INPUTS
    -df: pandas dataframe containing the data to plot
    OUTPUTS
    """

    column_names = df.columns
    row = df.index[0]
    to_search = []
    x = []
    y = []

    for i in column_names:
        if i.startswith("LE_"):
            to_search.append(i)
        else:
            continue

    list_130 = return_130(df, to_search)

    for j in list_130:
        to_remove = to_search[j]
        df = df.drop(to_remove, axis = 1)

    column_names = df.columns

    for k in column_names:
        if k.startswith("LE_"):
            x.append(int(k.lstrip("LE_")))
            y.append(df[k][row])

        else:
            continue

    ID = df["Participant_ID"][row]
    name = df["Protocol name"][row]
    condition = df["Protocol condition"][row]
    title = ID + " -- " + name + ": " + condition + " (Left Ear)"
    labels = {"title": title, "x": "Frequency (Hz)", "y": "Hearing Threshold (dB HL)"}

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = x,
                             y = y,
                             line_color = "blue",
                             mode = 'lines+markers',
                             name = title,
                             hovertemplate = "%{x:1.0f} Hz<br>" +
                                             "%{y:1.0f} dB HL"))
    fig.update_layout(title = labels["title"],
                      xaxis_title = labels["x"],
                      yaxis_title = labels["y"],
                      xaxis_type = "log",
                      xaxis_range = [np.log10(100), np.log10(20000)],
                      yaxis_range = [80, -20],
                      xaxis_showline = True,
                      xaxis_linecolor = "black",
                      yaxis_showline = True,
                      yaxis_linecolor = "black",
                      yaxis_zeroline = True,
                      yaxis_zerolinewidth = 1,
                      yaxis_zerolinecolor = "black")
    fig.show()



    #fig.write_image("../results/" + title + ".png")
