import pandas as pd

def rem_outlier(df, cols, n_stdv=3):
    """
    Takes in a Dataframe and removes from a column outliers of n standard deviations
    -----------------------------------------------------------------
    params:
        df = pandas DataFrame
        col = column(s) to remove outliers (type can be string or list of strings)
        n_stdv = # of standard deviations (default=3)
    """    
    assert type(df) == pd.core.frame.DataFrame, "df must be of type: pandas.DataFrame"
    
    if type(cols) == list: # col as a list of strings
        assert all([type(s) == str for s in cols]), "cols must be list of strings"
        new_df = df
        for s in cols:   # repeats len(cols) times
            new_df = rem_outlier(new_df, s, n_stdv)

    else:
        assert type(cols) == str, "cols must be string"
        new_df = pd.DataFrame()
        new_df = pd.concat([new_df, df.loc[(df[cols] - df[cols].mean()).abs() / df[cols].std() < n_stdv]])
    
    return new_df