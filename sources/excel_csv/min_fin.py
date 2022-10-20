import pandas as pd


def import_min_fin():
    """
    Import data from the ministry of finance regarding spending.
    :return:
    """

    df = pd.read_csv("C:\\Users\\Admin\\Desktop\\MinFin_Payments\\1a0ac2cc-2503-49dd-ac3c-4abe0b82fb3c\\SEBRA\\SEBRA.csv",
                     nrows=10000)


    print(df.head())
    return df


if __name__ == '__main__':

    df = import_min_fin()
    print(df.head())
