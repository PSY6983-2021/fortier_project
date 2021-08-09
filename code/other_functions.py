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

def plot_graph(df, test_type, ear = "Bilateral"):
    """
    INPUTS
    -df: pandas dataframe containing the data to plot
    -test_type: takes a str value that can either be \"pta\" or \"mtx\"
    -ear: takes a str with the ear side to plot ([Right, Left, Bilateral], default is Bilateral)
    OUTPUTS
    """
    counter = 0

    if test_type == "pta":
        if ear == "Right":
            x_columns = ["RE_250", "RE_500", "RE_1000", "RE_2000",
                         "RE_3000", "RE_4000", "RE_6000", "RE_8000",
                         "RE_9000", "RE_10000", "RE_11200", "RE_12500",
                         "RE_14000", "RE_16000", "RE_18000", "RE_20000"]
            x_labels = {"RE_250": 250, "RE_500": 500, "RE_1000": 1000, "RE_2000": 2000,
                        "RE_3000": 3000, "RE_4000": 4000, "RE_6000": 6000, "RE_8000": 8000,
                        "RE_9000": 9000, "RE_10000": 10000, "RE_11200": 11200, "RE_12500": 12500,
                        "RE_14000": 14000, "RE_16000": 16000, "RE_18000": 18000, "RE_20000": 20000}
        elif ear == "Left":
            x_columns = ["LE_250", "LE_500", "LE_1000", "LE_2000",
                         "LE_3000", "LE_4000", "LE_6000", "LE_8000",
                         "LE_9000", "LE_10000", "LE_11200", "LE_12500",
                         "LE_14000", "LE_16000", "LE_18000", "LE_20000"]
        elif ear == "Bilateral":
            x1_columns = ["RE_250", "RE_500", "RE_1000", "RE_2000",
                          "RE_3000", "RE_4000", "RE_6000", "RE_8000",
                          "RE_9000", "RE_10000", "RE_11200", "RE_12500",
                          "RE_14000", "RE_16000", "RE_18000", "RE_20000"]
            x2_columns = ["LE_250", "LE_500", "LE_1000", "LE_2000",
                          "LE_3000", "LE_4000", "LE_6000", "LE_8000",
                          "LE_9000", "LE_10000", "LE_11200", "LE_12500",
                          "LE_14000", "LE_16000", "LE_18000", "LE_20000"]
        else:
            print("ERROR: the test_type value isn't valid")

        i = 0
        data_y = df.loc[i, x_columns]
        data_y = data_y.reset_index(drop = True)
        data_y.columns = ["Hearing Threshold (dB HL)"]
        print(data_y)
        data_x = pd.DataFrame(data = [250, 500, 1000, 2000, 3000, 4000, 6000, 8000,
                                      9000, 10000, 11200, 12500, 14000, 16000, 18000, 20000])
        print(data_x)
        data = data_x.append(data_y)
        data.columns = ["Frequency (Hz)", "Hearing Threshold (dB HL)"]
        print(data)
        print(data.columns)
        data.to_csv("../results/data_test.csv")
        to_drop = []
        #print(data.index)
        for j in data.index:
            #print(j)
            #print(to_drop)
            #print(data.index[j])
            #print(df[column_to_search][i])
            #print(df[column_to_search][i] == value_to_search)
            if data[j] == 130:
                to_drop.append(j)
            else:
                continue
        #print(to_drop)
        data = data.drop(to_drop, axis = 0)
        #print(data)
        #return df.drop(to_drop, axis = 0)

        ID = df["Participant_ID"][i]
        name = df["Protocol name"][i]
        title = ID + "-" + name + " (" + ear + ")"
        #labels = {index: "Frequency (Hz)", value: "Hearing Threshold (dB HL)"}
        fig = px.line(data, title = title, log_x = True, range_x = [100, 20000], range_y = [-20, 80])
        fig.show()
        fig.write_image("../results/" + title + ".png")
        counter =+ 1
        #pass
    elif test_type == "mtx":
        pass
    else:
        print("The test_type value is not valid. The only valid values are str containing the value \"pta\" or the value \"mtx\".")
        pass

    if counter <= 1:
        print(counter, ".png file was saved.")
    else:
        print(counter, ".png files were saved.")
