# read env file
from dotenv import dotenv_values
from pathlib import Path
# import os

# load environment variables
env_path = Path("./.env")
config = dotenv_values(env_path)

USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]
HOST = config["HOST"]
PORT = config["PORT"]
DATABASE = config["DATABASE"]

if __name__ == "__main__":
    print("done")