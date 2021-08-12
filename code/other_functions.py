import numpy as np
import pandas as pd
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

    to_drop = []

    for i in range (0, len(df)):
        if df[column_to_search][i] == value_to_search:
            to_drop.append(i)
        else:
            continue
    df = df.drop(to_drop, axis = 0)
    df = df.reset_index(drop = True)
    return df


def save_graph(graph, df, ear):
    """
    INPUTS
    -graph: interactive plotly.graph_objects figure
    -df: dataframe with the informations that were used to generate the graph
    -ear: ear side linked with the graph
    OUTPUTS
    -saves the graph in a .html file to a subject's specific location in the repository
    """

    row = df.index[0]
    sub_long = df["Participant_ID"][row]
    sub_short = sub_long.lstrip("Sub")
    session = df["DATE"][row]
    name = df["Protocol name"][row]
    condition = df["Protocol condition"][row]
    folder = "../results/" + sub_long + "/"
    path = folder + "Sub-" + sub_short + "_" + session + "_" + name + ": " + condition + " (" + ear + ")" + ".html"
    graph.write_html(path)
    return True


def return_130(df, to_search):

    index_value = df.index[0]
    to_drop = []

    for i in to_search:
        if df[i][index_value] == 130:
            to_drop.append(to_search.index(i))
        else:
            continue
    return to_drop


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
    title = ID + " - " + name + ": " + condition + " (Left Ear)"
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
    #fig.show()

    completed = save_graph(fig, df, "Left Ear")
    if completed == True:
        return True
    else:
        return False


def plot_pta_R(df):
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
        if i.startswith("RE_"):
            to_search.append(i)
        else:
            continue

    list_130 = return_130(df, to_search)

    for j in list_130:
        to_remove = to_search[j]
        df = df.drop(to_remove, axis = 1)

    column_names = df.columns

    for k in column_names:
        if k.startswith("RE_"):
            x.append(int(k.lstrip("RE_")))
            y.append(df[k][row])
        else:
            continue

    ID = df["Participant_ID"][row]
    name = df["Protocol name"][row]
    condition = df["Protocol condition"][row]
    title = ID + " - " + name + ": " + condition + " (Right Ear)"
    labels = {"title": title, "x": "Frequency (Hz)", "y": "Hearing Threshold (dB HL)"}

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = x,
                             y = y,
                             line_color = "red",
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
    #fig.show()

    completed = save_graph(fig, df, "Right Ear")
    if completed == True:
        return True
    else:
        return False
