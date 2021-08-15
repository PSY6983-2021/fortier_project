import pandas as pd
import other_functions as of

if __name__ == "__main__":
    #url_share = input("Please input the URL of the Google Spreadsheet data file: ")
    url_share = "https://docs.google.com/spreadsheets/d/1UQsU6FNr7ovVjLRIMItgtYWr1zN7UHpMjfHtdGa1myc/edit#gid=0"
    url_csv =  url_share.replace("/edit#gid=", "/export?format=csv&gid=")
    master_data = pd.read_csv(url_csv)
    subjects = ["Sub01", "Sub02", "Sub03", "Sub04", "Sub05", "Sub06"]

    data_pta = master_data[["Participant_ID", "DATE", "Protocol name",
                            "Protocol condition", "Scan type",
                            "RE_250", "RE_500", "RE_1000",
                            "RE_2000", "RE_3000", "RE_4000",
                            "RE_6000", "RE_8000", "RE_9000",
                            "RE_10000", "RE_11200", "RE_12500",
                            "RE_14000", "RE_16000", "RE_18000",
                            "RE_20000", "LE_250", "LE_500",
                            "LE_1000", "LE_2000", "LE_3000",
                            "LE_4000", "LE_6000", "LE_8000",
                            "LE_9000", "LE_10000", "LE_11200",
                            "LE_12500", "LE_14000", "LE_16000",
                            "LE_18000", "LE_20000"]]

    data_pta_R = master_data[["Participant_ID", "DATE", "Protocol name",
                              "Protocol condition", "Scan type",
                              "RE_250", "RE_500", "RE_1000",
                              "RE_2000", "RE_3000", "RE_4000",
                              "RE_6000", "RE_8000", "RE_9000",
                              "RE_10000", "RE_11200", "RE_12500",
                              "RE_14000", "RE_16000", "RE_18000",
                              "RE_20000"]]

    data_pta_L = master_data[["Participant_ID", "DATE", "Protocol name",
                              "Protocol condition", "Scan type",
                              "LE_250", "LE_500", "LE_1000",
                              "LE_2000", "LE_3000", "LE_4000",
                              "LE_6000", "LE_8000", "LE_9000",
                              "LE_10000", "LE_11200", "LE_12500",
                              "LE_14000", "LE_16000", "LE_18000",
                              "LE_20000"]]


    data_mtx = master_data[["Participant_ID", "DATE", "Protocol name",
                            "Protocol condition", "Scan type",
                            "MTX_LANG_1", "MTX1_L_L", "MTX1_L_Bin",
                            "MTX1_Bin_Bin", "MTX1_R_Bin", "MTX1_R_R",
                            "MTX_LANG_2", "MTX2_L_L", "MTX2_L_Bin",
                            "MTX2_Bin_Bin", "MTX2_R_Bin", "MTX2_R_R"]]

    # Elimination of the lines that are irrelevant to each of the tests:
    # Matrix speech perception test
    data_mtx = of.eliminate_row(data_mtx, "Protocol name", "Baseline 1")
    data_mtx = of.eliminate_row(data_mtx, "Protocol condition", "Condition 3A (OAEs right before the scan)")
    data_mtx = of.eliminate_row(data_mtx, "Protocol condition", "Supplementary PTA test (Baseline)")
    data_mtx = of.eliminate_row(data_mtx, "Protocol condition", "Supplementary PTA test (right before the scan)")
    data_mtx = of.eliminate_row(data_mtx, "Protocol condition", "Supplementary PTA test (right after the scan)")

    # Pure-tone audiometry
    data_pta = of.eliminate_row(data_pta, "Protocol condition", "Condition 3A (OAEs right before the scan)")
    data_pta_L = of.eliminate_row(data_pta_L, "Protocol condition", "Condition 3A (OAEs right before the scan)")
    data_pta_R = of.eliminate_row(data_pta_R, "Protocol condition", "Condition 3A (OAEs right before the scan)")

    # Counter initialisation to keep track of the amount of files generated
    counter = 0
    save_error = 0

    # Generation of the interactive graphs (.html file format)
    # PTA, Left ear
    for i in range (0, len(data_pta_L)):
        action_i = of.plot_pta_L(data_pta_L.loc[[i]])
        if action_i == True:
            counter = counter + 1
        else:
            save_error = save_error + 1

    # PTA, Right ear
    for j in range (0, len(data_pta_R)):
        action_j = of.plot_pta_R(data_pta_R.loc[[j]])
        if action_j == True:
            counter = counter + 1
        else:
            save_error = save_error + 1

    # PTA, All results for one participant in one graph
    for k in subjects:
        one_subject = of.extract_subject(data_pta, k)
        action_k = of.plot_pta_subject(one_subject)
        if action_k == True:
            counter = counter + 1
        else:
            save_error = save_error + 1

    """
    for m in range (0, len(data_mtx)):
        action_m = of.plot_mtx(data_mtx[m])
        if action_m == True:
            counter = counter + 1
        else:
            save_error = save_error + 1
    """

    # Return a feedback to the user regarding the number of files created
    if counter <= 1:
        print(counter, ".html file was saved.")
        print(save_error, "file(s) was/were not properly saved")
    else:
        print(counter, ".html files were saved.")
        print(save_error, "file(s) was/were not properly saved")
