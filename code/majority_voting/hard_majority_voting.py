import os

import pandas as pd


def read_predictions_folder(folder):
    """
        Reads all the files in the given folder and returns a list of pandas data frames. (one for each file)
    """
    res = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path) and path.endswith(".csv"):
            df = pd.read_csv(path)
            df = df.set_index(['id'])
            res.append(df)
    return res


if __name__ == "__main__":
    predictions = read_predictions_folder("code/majority_voting/predictions")
    df_merged = pd.concat(predictions, axis=1)
    print("majority voting in progress...")
    df_merged['majority'] = df_merged.mode(axis=1)[0] # majority voting, see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html
    final_df = df_merged[['majority']]
    final_df = final_df.rename(columns={"majority": "prediction"})
    final_df.to_csv("code/majority_voting/majority_voting.csv")
