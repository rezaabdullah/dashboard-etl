import logging
import pandas as pd

# logging config
logging.basicConfig(filename="./log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.ERROR)

# extract sale dataset
def sale(engine):
    """
    read gds_sale_transactions table from sql database and returns df
    :param engine: SQLAlchemy engine object
    :return df: sale dataframe
    """
    
    try:
        with engine.connect() as conn:
            query = """
                SELECT country_name, parent_name, user_type, user_region, user_name, user_id, market_type,
                    business_category, category, product, transaction_date, transaction_id, customer_id, customer_name,
                    customer_mobile, customer_gender, product_amount, net_amount, due_amount, cogs_amount, version,
                    currency_exchange_rate
                FROM (
                    SELECT distinct user_id, country_name, user_name, user_type, parent_name, transaction_id,
                        transaction_date, customer_id, customer_name, customer_mobile, customer_gender,
                        market_type, sale_type, business_category, category_id, category, product_id, product,
                        unit_type, attribute, quantity, unit_price, product_amount, sub_total_amount,
                        commission_amount, discount_amount, net_amount, paid_amount, due_amount, due_receivable_date,
                        version, user_join_date, user_region, customer_join_date, currency_exchange_rate, cogs_amount
                    FROM gds_database.gds_sale_transactions
                    WHERE year(transaction_date) >= 2019
                ) sale;
                """
            df = pd.read_sql(query, conn)
    except Exception as e:
        logging.error(e)
        
    return df

# extract machine rent dataset
def machine_rent(engine):
    """
    read gds_machine_rent_transactions table from sql database and returns df
    :param engine: SQLAlchemy engine object
    :return df: sale dataframe
    """
    
    try:
        with engine.connect() as conn:
            query = """
                SELECT country_name, parent_name, user_type, user_region, user_name, user_id, business_category,
                    category, product, transaction_date, transaction_id, customer_id, customer_name,
                    customer_mobile, customer_gender, amount, net_amount, due_amount, version, currency_exchange_rate
                FROM (
                    SELECT distinct user_id, country_name, user_name, user_type, parent_name, transaction_id,
                        transaction_date, customer_id, customer_name, customer_mobile, customer_gender,
                        business_category, category_id, category, product_id, product, unit_type, quantity,
                        unit_price, unit_count, amount, sub_total_amount, net_amount, paid_amount, due_amount,
                        due_receivable_date, land_type, land_size, start_date_time, end_date_time, rent_hour,
                        version, user_join_date, user_region, customer_join_date, currency_exchange_rate
                    FROM gds_database.gds_machine_rent_transactions
                    WHERE year(transaction_date) >= 2019
                ) machine_rent;
                """
            df = pd.read_sql(query, conn)
    except Exception as e:
        logging.error(e)
        
    return df

# extract advisory dataset
def advisory(engine):
    """
    read advisory table from sql database and returns df
    :param engine: SQLAlchemy engine object
    :return df: sale dataframe
    """
    try:
        with engine.connect() as conn:
            query = """
                SELECT country_name, parent_name, user_type, user_region, user_name, user_id, business_categories,
                    categories, transaction_date, transaction_id, customer_id, customer_name, customer_mobile,
                        customer_gender, amount, version, currency_exchange_rate
                FROM (
                    SELECT distinct user_id, country_name, user_name, user_type, user_join_date, user_region,
                        parent_name, transaction_id, transaction_date, customer_id, customer_name, customer_mobile,
                        customer_gender, customer_join_date, categories_ids, business_categories, categories,
                        tags_ids, tags, comments, amount, usd_amount, version, currency_exchange_rate
                    FROM gds_database.gds_advisory_transactions
                    WHERE year(transaction_date) >= 2019
                ) advisory;
                """
            df = pd.read_sql(query, conn)
    except Exception as e:
        logging.error(e)
        
    return df

# extract purchase dataset
def purchase(engine):
    """
    read purchase table from sql database and returns df
    :param engine: SQLAlchemy engine object
    :return df: sale dataframe
    """
    try:
        with engine.connect() as conn:
            query = """
                SELECT country_name, parent_name, user_type, user_region, user_name, user_id, market_type,
                    business_category, category, product, transaction_date, transaction_id, supplier_id, supplier_name,
                    supplier_mobile, supplier_gender, product_amount, net_amount, due_amount, version,
                    currency_exchange_rate
                FROM (
                    SELECT distinct user_id, country_name, user_name, user_type, parent_name, transaction_id,
                        transaction_date, supplier_id, supplier_name, supplier_mobile, supplier_gender, market_type,
                        business_category, category_id, category, product_id, product, unit_type, attribute, quantity,
                        unit_price, product_amount, sub_total_amount, commission_amount, net_amount, paid_amount,
                        due_amount, due_payable_date, version, user_join_date, user_region, supplier_join_date,
                        currency_exchange_rate
                    FROM gds_database.gds_purchase_transactions
                    WHERE year(transaction_date) >= 2019
                ) purchase;
                """
            df = pd.read_sql(query, conn)
    except Exception as e:
        logging.error(e)
        
    return df

# extract processing dataset
def processing(engine):
    """
    read processing table from sql database and returns df
    :param engine: SQLAlchemy engine object
    :return df: sale dataframe
    """
    try:
        with engine.connect() as conn:
            query = """
                SELECT country_name, parent_name, user_type, user_region, user_name, user_id, business_category,
                    category, product, transaction_date, transaction_id, amount, production_cost, version,
                    currency_exchange_rate
                FROM (
                    SELECT distinct user_id, country_name, user_name, user_type, parent_name, transaction_id,
                        transaction_date, business_category, category_id, category, product_id, product, unit_type,
                        quantity, unit_price, amount, production_cost, version, user_join_date, user_region,
                        currency_exchange_rate
                    FROM gds_database.gds_processing_transactions
                    WHERE year(transaction_date) >= 2019
                ) processing;
                """
            df = pd.read_sql(query, conn)
    except Exception as e:
        logging.error(e)
        
    return df

# extract machine purchase dataset
def machine_purchase(engine):
    """
    read machine_purchase table from sql database and returns df
    :param engine: SQLAlchemy engine object
    :return df: sale dataframe
    """
    try:
        with engine.connect() as conn:
            query = """
                SELECT country_name, parent_name, user_type, user_region, user_name, user_id, business_category,
                    category, product, transaction_date, transaction_id, supplier_id, supplier_name,
                    supplier_mobile, supplier_gender, total_amount, due_amount, version,
                    currency_exchange_rate
                FROM (
                    SELECT distinct user_id, country_name, user_name, user_type, parent_name, transaction_id,
                        transaction_date, supplier_id, supplier_name, supplier_mobile, supplier_gender,
                        business_category, category_id, category, product_id, product, quantity, unit_price,
                        total_amount, paid_amount, due_amount, due_payable_date, version, user_join_date, user_region,
                        supplier_join_date, currency_exchange_rate
                    FROM gds_database.gds_machine_purchase_transactions
                    WHERE year(transaction_date) >= 2019
                ) machine_purchase;
                """
            df = pd.read_sql(query, conn)
    except Exception as e:
        logging.error(e)
        
    return df

# extract expense dataset
def expense(engine):
    """
    read expense table from sql database and returns df
    :param engine: SQLAlchemy engine object
    :return df: sale dataframe
    """
    try:
        with engine.connect() as conn:
            query = """
                SELECT country_name, parent_name, user_type, user_region, user_name, user_id, expense_category,
                    business_category, product_category, expense_type, transaction_date, transaction_id, total_amount,
                    version, currency_exchange_rate
                FROM (
                    SELECT distinct user_id, country_name, user_name, user_type, parent_name, transaction_id,
                        transaction_date, expense_category, expense_type, total_amount, business_category,
                        product_category_id, product_category, version, user_join_date, user_region,
                        currency_exchange_rate
                    FROM gds_database.gds_expense_transactions
                    WHERE year(transaction_date) >= 2019
                ) expense;
                """
            df = pd.read_sql(query, conn)
    except Exception as e:
        logging.error(e)
        
    return df