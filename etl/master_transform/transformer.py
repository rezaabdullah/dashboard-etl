from xml.dom.pulldom import IGNORABLE_WHITESPACE
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
    
    # rename customer information with person prefix
    income.rename(columns={"customer_id":"person_id", "customer_name":"person_name",
        "customer_mobile":"person_mobile", "customer_gender":"person_gender"}, inplace=True)

    income.to_csv("income.csv", index=False)

    # filter expenditure generating dataset i.e. sale, machine rent and advisory
    expenditure = df.loc[df["transaction_category"].isin(["Purchase", "Machinery Purchase",
        "Processing"])]

    # drop unnecessary columns
    expenditure.drop(columns=["customer_id", "customer_name", "customer_mobile", "customer_gender",
        "product_amount", "product_amount_usd", "revenue", "revenue_usd", "cogs_amount",
        "cogs_amount_usd", "product_expenditure", "product_expenditure_usd",
        "expense_category", "direct_cost_usd", "indirect_cost_usd"], inplace=True)

    # rename supplier information with person prefix
    expenditure.rename(columns={"supplier_id":"person_id", "supplier_name":"person_name",
        "supplier_mobile":"person_mobile", "supplier_gender":"person_gender"}, inplace=True)

    expenditure.to_csv("expenditure.csv", index=False)

    # filter expenditure generating dataset i.e. sale, machine rent and advisory
    expenditure = df.loc[df["transaction_category"].isin(["Purchase", "Machinery Purchase",
        "Processing"])]

    # drop unnecessary columns
    expenditure.drop(columns=["customer_id", "customer_name", "customer_mobile", "customer_gender",
        "product_amount", "product_amount_usd", "revenue", "revenue_usd", "cogs_amount",
        "cogs_amount_usd", "product_expenditure", "product_expenditure_usd",
        "expense_category", "direct_cost_usd", "indirect_cost_usd"], inplace=True)

    # rename supplier information with person prefix
    expenditure.rename(columns={"supplier_id":"person_id", "supplier_name":"person_name",
        "supplier_mobile":"person_mobile", "supplier_gender":"person_gender"}, inplace=True)

    expenditure.to_csv("expenditure.csv", index=False)