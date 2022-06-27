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

    # filter expenditure generating dataset i.e. purchase, machinery purchase and processing
    expenditure = df.loc[df["transaction_category"].isin(["Purchase", "Machinery Purchase",
        "Processing"])]

    # drop unnecessary columns
    expenditure.drop(columns=["customer_id", "customer_name", "customer_mobile", "customer_gender",
        "product_amount", "product_amount_usd", "revenue", "revenue_usd", "cogs_amount",
        "cogs_amount_usd", "expense_category", "direct_cost_usd", "indirect_cost_usd"], inplace=True)

    # rename supplier information with person prefix
    expenditure.rename(columns={"supplier_id":"person_id", "supplier_name":"person_name",
        "supplier_mobile":"person_mobile", "supplier_gender":"person_gender"}, inplace=True)

    expenditure.to_csv("expenditure.csv", index=False)

    # filter expense generating dataset i.e. direct cost, indirect cost
    expense = df.loc[df["transaction_category"].isin(["Expense"])]

    # drop unnecessary columns
    expense.drop(columns=["customer_id", "customer_name", "customer_mobile", "customer_gender",
        "product_amount", "product_amount_usd", "revenue", "revenue_usd", "cogs_amount",
        "cogs_amount_usd", "due_amount", "supplier_id", "supplier_name", "supplier_mobile",
        "supplier_gender", "product_expenditure", "product_expenditure_usd"], inplace=True)

    expense.to_csv("expense.csv", index=False)

    # filter direct cost and indirect cost
    direct_cost = expense.loc[expense["expense_category"].isin(["Direct Cost"])]

    # drop transaction_category and rename expense_category to transaction_category
    direct_cost.drop(columns=["transaction_category", "expenditure_usd"], inplace=True)
    direct_cost.rename(columns={"expense_category":"transaction_category",
        "direct_cost_usd":"expenditure_usd"}, inplace=True)

    direct_cost.to_csv("direct_cost.csv", index=False)

    # filter direct cost and indirect cost
    indirect_cost = expense.loc[expense["expense_category"].isin(["Indirect Cost"])] 

    # drop transaction_category and rename expense_category to transaction_category
    indirect_cost.drop(columns=["transaction_category", "expenditure_usd"], inplace=True)
    indirect_cost.rename(columns={"expense_category":"transaction_category",
        "indirect_cost_usd":"expenditure_usd"}, inplace=True)

    indirect_cost.to_csv("indirect_cost.csv", index=False)