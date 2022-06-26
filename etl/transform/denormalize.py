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
    income["product_amount_usd"] = round(income["product_amount"] / 
        income["currency_exchange_rate"], 4)
    income["revenue_usd"] = round(income["revenue"] /
        income["currency_exchange_rate"], 4)
    income["cogs_amount_usd"] = round(income["cogs_amount"] / 
        income["currency_exchange_rate"], 4)
    
    # concat all cash-out transactions
    expenditure = pd.concat([purchase, machine_purchase, processing], sort=False, ignore_index=True)
    # usd conversion
    expenditure["product_expenditure_usd"] = round(expenditure["product_expenditure"] / 
        expenditure["currency_exchange_rate"], 4)
    expenditure["expenditure_usd"] = round(expenditure["expenditure"] /
        expenditure["currency_exchange_rate"], 4)

    # filter direct cost
    direct_cost = expense[expense["expense_category"] == "Direct Cost"]
    # usd conversion
    direct_cost_usd = round(direct_cost["expenditure"] /
        direct_cost["currency_exchange_rate"], 4)
    direct_cost = direct_cost.assign(direct_cost_usd = direct_cost_usd)

    # filter indirect cost
    indirect_cost = expense[expense["expense_category"] == "Indirect Cost"]
    # usd conversion
    indirect_cost_usd = round(indirect_cost["expenditure"] /
        indirect_cost["currency_exchange_rate"], 4)
    indirect_cost = indirect_cost.assign(indirect_cost_usd = indirect_cost_usd)

    # concatenate direct and indirect cost
    expense = pd.concat([direct_cost, indirect_cost], sort=False, ignore_index=True)
    expense.drop(columns=["expense_type"], inplace=True)

    df = pd.concat([income, expenditure, expense], sort=False, ignore_index=True)
    df.drop(columns=["business_categories", "categories"], inplace=True)

    df.to_csv("master_data.csv", index=False)

    return df