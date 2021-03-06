# directory management & environment file
from dotenv import dotenv_values
from pathlib import Path
import logging

# extract module
from extract import get_sale, get_machine_rent, get_advisory, get_purchase, \
    get_machine_purchase, get_processing, get_expense, get_user

# transform module
from module_transform import transform_sale, transform_advisory, transform_expense, \
    transform_machine_purchase, transform_machine_rent, transform_processing, \
    transform_purchase, transform_user
from module_transform import denormalize
from master_transform import master_transform
from master_transform import master_data_compiler
from master_transform import anomaly

# database toolkit
from sqlalchemy import create_engine, inspect
# MetaData, Table, Column, Integer, String, Date, Numeric, extract
from sqlalchemy.engine.url import URL
# from sqlalchemy.sql import select
import pandas as pd

# load environment variables
env_path = Path("./.env")
config = dotenv_values(env_path)

# logging config
logging.basicConfig(filename="./log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.ERROR)

def connect_db():
    try:
        # initiate connection to database
        connect_url = URL.create(
            "mysql+pymysql",
            username=config["USERNAME"],
            password=config["PASSWORD"],
            host=config["HOST"],
            port=config["PORT"],
            database=config["DATABASE"]
        )
        engine = create_engine(connect_url)

        # debug
        with engine.connect() as conn:
            inspector = inspect(engine)
            table_names = inspector.get_table_names()
            logging.debug(table_names)
        
        return engine
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    # connect to the database
    engine = connect_db()

    # extracting dataset
    logging.info("Extracting dataset")
    sale = get_sale(engine)
    machine_rent = get_machine_rent(engine)
    advisory = get_advisory(engine)
    purchase = get_purchase(engine)
    processing = get_processing(engine)
    machine_purchase = get_machine_purchase(engine)
    expense = get_expense(engine)
    user = get_user(engine)

    # transform datasets
    logging.info("Transforming dataset")
    sale = transform_sale(sale)
    machine_rent = transform_machine_rent(machine_rent)
    advisory = transform_advisory(advisory)
    purchase = transform_purchase(purchase)
    processing = transform_processing(processing)
    machine_purchase = transform_machine_purchase(machine_purchase)
    expense = transform_expense(expense)
    user = transform_user(user)

    # denormalize dataset
    df = denormalize(sale, machine_rent, advisory, purchase, machine_purchase, processing, expense)
    
    # find data anomaly and filter the anomalous data
    main_df = master_transform(df)

    # transform and join user data
    main_df = master_data_compiler(main_df, user)

    clean_df, anomaly = anomaly(main_df)
    clean_df.to_csv("clean_df.csv", index=False)
    anomaly.to_csv("anomaly.csv", index=False)