import pandas as pd

# transform sale dataset
def transform_sale(df):
    """
    transform sale dataframe and returns df
    :param df: actual sale dataframe
    :return df: transformed dataframe
    """
    
    # drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)
    
    # convert date_of_transaction to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y/%m/%d")

    # convert user_id to string
    df["user_id"] = df["user_id"].astype(str)
    df["customer_id"] = df["customer_id"].astype(str)
    df["customer_mobile"] = df["customer_mobile"].astype(str)
    df["transaction_id"] = df["transaction_id"].astype(str)

    # convert and round numerical columns
    df["product_amount"] = df["product_amount"].astype(float)
    df["net_amount"] = df["net_amount"].astype(float)
    df["cogs_amount"] = df["cogs_amount"].astype(float)
    df["due_amount"] = df["due_amount"].astype(float)
    df["currency_exchange_rate"] = df["currency_exchange_rate"].astype(float)

    # renaming columns for consistency
    df.rename(columns={"net_amount" : "revenue"}, inplace=True)

    # add transaction_category column to identify the module used for transaction
    df["transaction_category"] = "Sale"

    # sorting data based on version and keep the latest version only
    df = df.sort_values(["country_name", "parent_name", "user_id", "transaction_id", "category", "product",
            "version"]) \
        .drop_duplicates(subset=["transaction_id", "category", "product"], keep="last")

    return df

# transform machine rent dataset
def transform_machine_rent(df):
    """
    transform machine_rent dataframe and returns df
    :param df: actual machine_rent dataframe
    :return df: transformed dataframe
    """
    # drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)

    # convert date_of_transaction to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y/%m/%d")

    # convert user_id to string
    df["user_id"] = df["user_id"].astype(str)
    df["customer_id"] = df["customer_id"].astype(str)
    df["customer_mobile"] = df["customer_mobile"].astype(str)
    df["transaction_id"] = df["transaction_id"].astype(str)

    # convert and round numerical columns
    df["amount"] = df["amount"].astype(float)
    df["net_amount"] = df["net_amount"].astype(float)
    df["due_amount"] = df["due_amount"].astype(float)
    df["currency_exchange_rate"] = df["currency_exchange_rate"].astype(float)
    
    # renaming columns for consistency
    df.rename(columns={"net_amount" : "revenue",
        "amount": "product_amount"}, inplace=True)

    # add market_type column
    df["market_type"] = "Farmer"
    df["transaction_category"] = "Machinery Rental"

    # sorting data based on version and keep the latest version only
    df = df.sort_values(["country_name", "parent_name", "user_id", "transaction_id", "category", "product",
            "version"]) \
        .drop_duplicates(subset=["transaction_id", "category", "product"], keep="last")

    return df

# transform advisory dataset
def transform_advisory(df):
    """
    transform advisory dataframe and returns df
    :param df: actual machine_rent dataframe
    :return df: transformed dataframe
    """
    
    # drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)

    # convert date_of_transaction to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y/%m/%d")

    # convert user_id to string
    df["user_id"] = df["user_id"].astype(str)
    df["customer_id"] = df["customer_id"].astype(str)
    df["customer_mobile"] = df["customer_mobile"].astype(str)
    df["transaction_id"] = df["transaction_id"].astype(str)

    # convert and round numerical columns
    df["amount"] = df["amount"].astype(float)
    df["currency_exchange_rate"] = df["currency_exchange_rate"].astype(float)
    
    # renaming columns for consistency
    df.rename(columns={"amount" : "revenue"}, inplace=True)

    # add market_type column
    df["market_type"] = "Farmer"
    df["transaction_category"] = "Advisory"
    df["business_category"] = "Advisory"
    df["category"] = "Advisory"

    # sorting data based on version and keep the latest version only
    df = df.sort_values(["country_name", "parent_name", "user_id", "transaction_id", "category",
        "version"]) \
        .drop_duplicates(subset=["transaction_id", "category"], keep="last")

    return df

# transform purchase dataset
def transform_purchase(df):
    """
    transform purchase dataframe and returns df
    :param df: actual purchase dataframe
    :return df: transformed dataframe
    """
    # drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)
    
    # convert transaction_date to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y/%m/%d")

    # convert user_id to string
    df["user_id"] = df["user_id"].astype(str)
    df["supplier_id"] = df["supplier_id"].astype(str)
    df["supplier_mobile"] = df["supplier_mobile"].astype(str)
    df["transaction_id"] = df["transaction_id"].astype(str)

    # convert and round numerical columns
    df["net_amount"] = df["net_amount"].astype(float)
    df["due_amount"] = df["due_amount"].astype(float)   
    df["currency_exchange_rate"] = df["currency_exchange_rate"].astype(float)

    # renaming columns for consistency
    df.rename(columns={"net_amount" : "expenditure",
        "product_amount" : "product_expenditure"}, inplace=True)

    # add market_type column
    df["transaction_category"] = "Purchase"

    # sorting data based on version and keep the latest version only
    df = df.sort_values(["country_name", "parent_name", "user_id", "transaction_id", "category", "product",
            "version"]) \
        .drop_duplicates(subset=["transaction_id", "category", "product"], keep="last")

    return df

# transform processing dataset
def transform_processing(df):
    """
    transform processing dataframe and returns df
    :param df: actual processing dataframe
    :return df: transformed dataframe
    """
    # drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)
    
    # convert transaction_date to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y/%m/%d")

    # convert user_id to string
    df["user_id"] = df["user_id"].astype(str)
    df["transaction_id"] = df["transaction_id"].astype(str)

    # convert and round numerical columns
    df["amount"] = df["amount"].astype(float)
    df["production_cost"] = df["production_cost"].astype(float)
    df["currency_exchange_rate"] = df["currency_exchange_rate"].astype(float)

    # renaming columns for consistency
    df.rename(columns={"production_cost" : "expenditure",
        "amount" : "product_expenditure"}, inplace=True)

    # add transaction category column
    df["market_type"] = df["user_type"]
    df["transaction_category"] = "Processing"

    # sorting data based on version and keep the latest version only
    df = df.sort_values(["country_name", "parent_name", "user_id", "transaction_id", "category", "product",
            "version"]) \
        .drop_duplicates(subset=["transaction_id", "category", "product"], keep="last")

    return df

# transform machine purchase dataset
def transform_machine_purchase(df):
    """
    transform machine_purchase dataframe and returns df
    :param df: actual machine_purchase dataframe
    :return df: transformed dataframe
    """
    # drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)
    
    # convert transaction_date to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y/%m/%d")

    # convert user_id to string
    df["user_id"] = df["user_id"].astype(str)
    df["supplier_id"] = df["supplier_id"].astype(str)
    df["supplier_mobile"] = df["supplier_mobile"].astype(str)
    df["transaction_id"] = df["transaction_id"].astype(str)

    # convert and round numerical columns
    df["total_amount"] = df["total_amount"].astype(float)
    df["due_amount"] = df["due_amount"].astype(float)
    df["currency_exchange_rate"] = df["currency_exchange_rate"].astype(float)    

    # usd conversion
    df.rename(columns={"total_amount" : "expenditure"}, inplace=True)

    # add transaction category column
    df["market_type"] = df["user_type"]
    df["transaction_category"] = "Machinery Purchase"

    # sorting data based on version and keep the latest version only
    df = df.sort_values(["country_name", "parent_name", "user_id", "transaction_id", "category", "product",
            "version"]) \
        .drop_duplicates(subset=["transaction_id"], keep="last")

    return df

# transform expense dataset
def transform_expense(df):
    """
    transform expense dataframe and returns df
    :param df: actual expense dataframe
    :return df: transformed dataframe
    """
    # drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)
    
    # convert transaction_date to datetime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%Y/%m/%d")

    # convert user_id to string
    df["user_id"] = df["user_id"].astype(str)
    df["transaction_id"] = df["transaction_id"].astype(str)

    # convert and round numerical columns
    df["total_amount"] = df["total_amount"].astype(float)
    df["currency_exchange_rate"] = df["currency_exchange_rate"].astype(float)

    # revenue & profit
    df.rename(columns={"total_amount" : "expenditure",
        "product_category" : "category"}, inplace=True)

    # add transaction category column
    df["market_type"] = df["user_type"]
    df["transaction_category"] = "Expense"

    # sorting data based on version and keep the latest version only
    df = df.sort_values(["country_name", "parent_name", "user_id", "transaction_id", "expense_category",
            "category", "expense_type", "version"]) \
        .drop_duplicates(subset=["transaction_id", "expense_category", "category", "expense_type"],
            keep="last")

    return df

# transform user dataset
def transform_user(df):
    """
    transform user dataframe and returns df
    :param df: actual user dataframe
    :return df: transformed dataframe
    """

    # drop unnecessary columns
    df.drop(columns=["id", "created_at", "updated_at"], inplace=True)

    # rename columns for consistency
    df.rename(columns={"country":"country_name", "region":"user_region",
        "branch":"user_branch", "enterprise_name":"user_name",
        "parent_franchisee":"parent_name", "lat":"latitude",
        "long":"longitude"}, inplace=True)

    # define column types
    df["user_id"] = df["user_id"].astype(str)
    df["latitude"] = round(pd.to_numeric(df["latitude"], errors="coerce"), 6)
    df["longitude"] = round(pd.to_numeric(df["longitude"], errors="coerce"), 6)
    df["dropout_at"] = pd.to_datetime(df["dropout_at"], format="%Y/%m/%d")

    return df