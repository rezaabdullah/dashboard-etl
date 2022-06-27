import pandas as pd

# normalize dataset for granular analysis
def master_transform(df):
    """
    transform master dataset
    :param df: main dataset
    :return df: transformed dataset
    """
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

    # filter expense generating dataset i.e. direct cost, indirect cost
    expense = df.loc[df["transaction_category"].isin(["Expense"])]

    # drop unnecessary columns
    expense.drop(columns=["customer_id", "customer_name", "customer_mobile", "customer_gender",
        "product_amount", "product_amount_usd", "revenue", "revenue_usd", "cogs_amount",
        "cogs_amount_usd", "due_amount", "supplier_id", "supplier_name", "supplier_mobile",
        "supplier_gender", "product_expenditure", "product_expenditure_usd"], inplace=True)

    # filter direct cost and indirect cost
    direct_cost = expense.loc[expense["expense_category"].isin(["Direct Cost"])]

    # drop transaction_category and rename expense_category to transaction_category
    direct_cost.drop(columns=["transaction_category", "expenditure_usd",
        "indirect_cost_usd", "product"], inplace=True)
    direct_cost.rename(columns={"expense_category":"transaction_category",
        "direct_cost_usd":"expenditure_usd"}, inplace=True)

    # filter direct cost and indirect cost
    indirect_cost = expense.loc[expense["expense_category"].isin(["Indirect Cost"])] 

    # drop transaction_category and rename expense_category to transaction_category
    indirect_cost.drop(columns=["transaction_category", "expenditure_usd",
        "direct_cost_usd", "business_category", "category", "product"], inplace=True)
    indirect_cost.rename(columns={"expense_category":"transaction_category",
        "indirect_cost_usd":"expenditure_usd"}, inplace=True)

    # append indirect and direct cost
    expense = pd.concat([direct_cost, indirect_cost], sort=False, ignore_index=True)

    # append expenditure with expense
    expenditure = pd.concat([expenditure, expense], sort=False, ignore_index=True)

    # append expenditure with income
    df = pd.concat([income, expenditure], sort=False, ignore_index=True)

    return df

# join user dataset with master dataset
def compile_data(main_df, user_df):
    """
    join two dataframe and create a unified dataset
    :param main_df: master dataset
    :param user_df: user dataset
    :return df: joined dataset
    """
    user_main=main_df.loc[:, ["country_name", "parent_name", "user_region", "user_id",
        "user_name", "user_type"]]
    user_main.drop_duplicates(inplace=True)
    user_main.to_csv("user_main.csv", index=False)

    user_join = user_main.join(user_df, on="user_id", how="left") \
        [["country_name", "parent_name", "user_region", "user_id", "user_name", "user_type",
        "latitude", "longitude", "status"]]
    user_join.to_csv("user_join.csv", index=False)
    