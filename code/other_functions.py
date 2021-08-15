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


def extract_subject(df, subject):
    """
    INPUTS
    -df: dataframe containing all the tests
    -subject: ID of the participant to isolate
    OUTPUTS
    -returns a dataframe containing only the sessions linked to the ID provided
    """

    mask = df["Participant_ID"] == subject
    df_sub = df[mask].reset_index(drop = True)

    return df_sub


def save_graph_PTA(graph, df, ear):
    """
    INPUTS
    -graph: interactive plotly.graph_objects figure
    -df: dataframe with the informations that were used to generate the graph
    -ear: ear side linked with the graph
    OUTPUTS
    -saves the graph in a .html file to a subject's specific location in the repository
    """

    test = "PTA"

    row = df.index[0]

    sub_long = df["Participant_ID"][row]
    sub_short = sub_long.lstrip("Sub")

    folder = "../results/" + sub_long + "/"
    path_header = folder + "Sub-" + sub_short + "_" + test + "_"

    if ear == "All_runs":
        path = path_header + ear + ".html"

    else:
        session = df["DATE"][row]
        name = df["Protocol name"][row]
        condition = df["Protocol condition"][row]

        path = path_header + session + "_" + name + ": " + condition + " (" + ear + ")" + ".html"

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


def generate_title_graph(df, test):
    """
    INPUTS
    -df: dataframe with the informations to generate the title for a multiple runs graph
    OUTPUTS
    -returns a string to use as a title for the graph to generate
    """

    row = df.index[0]
    ID = df["Participant_ID"][row]
    #name = df["Protocol name"][row]
    #condition = df["Protocol condition"][row]

    if test == "PTA":
        title = ID + " - " + "Pure-Tone Audiometry"
    elif test == "MTX":
        title = ID + " - " + "Matrix Speech-in-Noise Perception Test"
    else:
        print("The test parameter passed to the generate_title_graph function is not valid.")

    return title


def generate_title_run(df, ear, index):
    """
    INPUTS
    -df: dataframe with the informations to generate the title for a single run
    -ear: ear side linked with the title
    OUTPUTS
    -returns a string to use as a title for the graph to generate
    """

    #print(df)
    ID = df["Participant_ID"][index]
    name = df["Protocol name"][index]
    condition = df["Protocol condition"][index]

    title = ID + " - " + name + ": " + condition + " (" + ear +")"

    return title


def data_to_plot(df, prefix):
    column_names = df.columns
    row = df.index[0]
    #print(len(df))
    to_search = []
    x = []
    y = []

    for i in column_names:
        if i.startswith(prefix):
            to_search.append(i)
        else:
            continue

    list_130 = return_130(df, to_search)

    for j in list_130:
        to_remove = to_search[j]
        df = df.drop(to_remove, axis = 1)

    column_names = df.columns

    for k in column_names:
        if k.startswith(prefix):
            x.append(int(k.lstrip(prefix)))
            y.append(df[k][row])
        else:
            continue

    #print("x:", x)
    #print("y:", y)
    return x, y


def plot_pta_L(df):
    """
    INPUTS
    -df: pandas dataframe containing the data to plot
    OUTPUTS
    -saves pta graphs in .html
    """

    x, y = data_to_plot(df, "LE_")

    title = generate_title_run(df, "Left Ear", df.index[0])

    labels = {"title": title, "x": "Frequency (Hz)", "y": "Hearing Threshold (dB HL)"}

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = x,
                             y = y,
                             line_color = "blue",
                             mode = 'lines+markers',
                             name = labels["title"],
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

    completed = save_graph_PTA(fig, df, "Left Ear")

    if completed == True:
        return True
    else:
        return False


def plot_pta_R(df):
    """
    INPUTS
    -df: pandas dataframe containing the data to plot
    OUTPUTS
    -saves pta graphs in .html
    """

    x, y = data_to_plot(df, "RE_")

    title = generate_title_run(df, "Right Ear", df.index[0])

    labels = {"title": title, "x": "Frequency (Hz)", "y": "Hearing Threshold (dB HL)"}

    fig = go.Figure()
    fig.add_trace(go.Scatter(x = x,
                             y = y,
                             line_color = "red",
                             mode = 'lines+markers',
                             name = labels["title"],
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

    completed = save_graph_PTA(fig, df, "Right Ear")

    if completed == True:
        return True
    else:
        return False


def plot_pta_subject(df):
    """
    INPUTS
    -df: pandas dataframe containing the data to plot
    OUTPUTS
    -saves pta graph in .html
    """

    title_graph = generate_title_graph(df, "PTA")
    labels = {"title": title_graph, "x": "Frequency (Hz)", "y": "Hearing Threshold (dB HL)"}

    fig = go.Figure()

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

    for i in range (0, len(df)):
        run_R_x, run_R_y = data_to_plot(df.loc[[i]], "RE_")
        run_L_x, run_L_y = data_to_plot(df.loc[[i]], "LE_")

        title_run_R = generate_title_run(df, "Right Ear", i)
        title_run_L = generate_title_run(df, "Left Ear", i)

        fig.add_trace(go.Scatter(x = run_R_x,
                                 y = run_R_y,
                                 line_color = "red",
                                 mode = 'lines+markers',
                                 name = title_run_R,
                                 hovertemplate = "%{x:1.0f} Hz<br>" +
                                                 "%{y:1.0f} dB HL"))

        fig.add_trace(go.Scatter(x = run_L_x,
                                 y = run_L_y,
                                 line_color = "blue",
                                 mode = 'lines+markers',
                                 name = title_run_L,
                                 hovertemplate = "%{x:1.0f} Hz<br>" +
                                                 "%{y:1.0f} dB HL"))


    #fig.show()
    completed = save_graph_PTA(fig, df, "All_runs")

    if completed == True:
        return True
    else:
        return False
