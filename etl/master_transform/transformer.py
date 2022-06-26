import pandas as pd

# normalize dataset for granular analysis
def transformer(df):
    # filter income generating dataset i.e. sale, machine rent and advisory
    cash_in = df.loc[df["transaction_category"].isin(["Sale", "Advisory",
        "Machinery Rental"])]
    
    cash_in.to_csv("cash_in.csv", index=False)
    return df