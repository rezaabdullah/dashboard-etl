import pandas as pd

# normalize dataset for granular analysis
def transformer(df):
    # filter income generating dataset i.e. sale, machine rent and advisory
    income = df.loc[df["transaction_category"].isin(["Sale", "Advisory",
        "Machinery Rental"])]

    # drop unnecessary columns
    income.drop(columns=["supplier_id", "supplier_name", "supplier_mobile", "supplier_gender",
        "product_expenditure", "expenditure", "product_expenditure_usd", "expenditure_usd",
        "expense_category", "direct_cost_usd", "indirect_cost_usd"], inplace=True)

    income.to_csv("income.csv", index=False)