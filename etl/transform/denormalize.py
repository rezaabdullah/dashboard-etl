import pandas as pd

def denormalize(sale, machine_rent, advisory, purchase, machine_purchase, processing, expense):
    """
    denormalize all the transactions i.e. concatanate or compile all the transactional tables into one
    master table
    :param sale: sale dataframe
    :param machine_rent: machine_rent dataframe
    :param advisory: advisory dataframe
    :param purchase: purchase dataframe
    :param machine_purchase: machine_purchase dataframe
    :param processing: processing dataframe
    :param expense: expense dataframe
    :return df: return master data
    """
    # concat all cash-in transactions
    income = pd.concat([sale, machine_rent, advisory], sort=False, ignore_index=True)
    # usd conversion
    income.loc[:, "product_amount_usd"] = round(income.loc[:, "product_amount"] / 
        income.loc[:, "currency_exchange_rate"], 4)
    income.loc[:, "revenue_usd"] = round(income.loc[:, "revenue"] /
        income.loc[:, "currency_exchange_rate"], 4)
    income.loc[:, "cogs_amount_usd"] = round(income.loc[:, "cogs_amount"] / 
        income.loc[:, "currency_exchange_rate"], 4)
    
    # concat all cash-out transactions
    expenditure = pd.concat([purchase, machine_purchase, processing], sort=False, ignore_index=True)
    # usd conversion
    expenditure.loc[:, "product_expenditure_usd"] = round(expenditure.loc[:, "product_expenditure"] / 
        expenditure.loc[:, "currency_exchange_rate"], 4)
    expenditure.loc[:, "expenditure_usd"] = round(expenditure.loc[:, "expenditure"] /
        expenditure.loc[:, "currency_exchange_rate"], 4)

    # filter direct cost
    direct_cost = expense.loc[expense.loc[:, "expense_category"] == "Direct Cost"]
    # usd conversion
    direct_cost.loc[:, "direct_cost_usd"] = round(direct_cost.loc[:, "expenditure"] /
        direct_cost.loc[:, "currency_exchange_rate"], 4)

    # filter indirect cost
    indirect_cost = expense.loc[expense["expense_category"] == "Indirect Cost"]
    # usd conversion
    indirect_cost.loc[:, "indirect_cost_usd"] = round(indirect_cost.loc[:, "expenditure"] /
        indirect_cost.loc[:, "currency_exchange_rate"], 4)

    # concatenate direct and indirect cost
    expense = pd.concat([direct_cost, indirect_cost], sort=False, ignore_index=True)
    expense.drop(columns=["expense_type"], inplace=True)

    df = pd.concat([income, expenditure, expense], sort=False, ignore_index=True)
    df.drop(columns=["business_categories", "categories"], inplace=True)

    df.to_csv("master_data.csv", index=False)

    return df