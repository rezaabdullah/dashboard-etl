# directory management & environment file
from dotenv import dotenv_values
from pathlib import Path
import logging

from extract import sale, machine_rent, advisory, purchase, machine_purchase, \
    processing, expense

# database toolkit
from sqlalchemy import create_engine, MetaData, inspect, Table, Column, Integer, \
    String, Date, Numeric, extract
from sqlalchemy.engine.url import URL
from sqlalchemy.sql import select

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
    engine = connect_db()

    # extracting data
    print("extracting data")
    sale = sale(engine)
    machine_rent = machine_rent(engine)
    advisory = advisory(engine)
    purchase = purchase(engine)
    processing = processing(engine)
    machine_purchase = machine_purchase(engine)
    expense = expense(engine)
    print(expense.head())