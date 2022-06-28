import pandas as pd
from fuzzywuzzy import fuzz

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

# defining a function to return the match and similarity score of the fuzz.ratio() scorer.
# the function will take in a term(name), list of terms(list_names), and a minimum
# similarity score(min_score) to return the match.
def similarity_score(name, list, min_score=0):
    max_score = -1
    max_name = ''
    for x in list:
        score = fuzz.ratio(name, x)
        if (score > min_score) & (score > max_score):
            max_name = x
            max_score = score
    return (max_name, max_score)

# join user dataset with master dataset
def master_data_compiler(main_df, user_df):
    """
    join two dataframe and create a unified dataset
    :param main_df: master dataset
    :param user_df: user dataset
    :return df: joined dataset
    """
    # find similar user_name from user dataset and update the user_name in main
    # dataset
    target_user_name=list(main_df.user_name.unique())
    source_user_name=list(user_df.user_name.unique())

    # for loop to create a list of tuples with the first value being the name from
    # the first dataframe (name to replace) and the second value from the second
    # dataframe (string replacing the name value). Then, casting the list of tuples
    # as a dictionary.
    names = []
    for x in target_user_name:
        match = similarity_score(x, source_user_name, 75)
        if match[1] >= 80:
            name = (str(x), str(match[0]))
            names.append(name)
    name_dict = dict(names)
    main_df.user_name = main_df.user_name.replace(name_dict)

    # join user dataset with main dataset
    main_df = main_df.merge(user_df[["user_id", "latitude", "longitude", "status",
        "dropout_at"]], on="user_id", how="left")

    return main_df