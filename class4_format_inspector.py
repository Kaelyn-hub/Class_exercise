import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    logger.info(f"Reading CSV File: {filepath}")
    df = pd.read_csv(filepath)
    print(df.head(3))

def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    logger.info(f"Reading JSON File: {filepath}")
    with open(filepath, "r") as f:
        data = json.load(f)
    print(data)

def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    logger.info(f"Reading YAML File: {filepath}")
    with open(filepath, "r") as f:
        config = yaml.safe_load(f)
    print(config)

def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()
    logger.info(".env file loaded")
    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]
    print(keys)

def main():
    file_path   = Path('data') / 'sample.csv'
    config_path = Path('data') / 'sample.yaml'
    json_path = Path('data') / 'sample.json'
    inspect_csv(file_path)
    inspect_yaml(config_path)
    inspect_json(json_path)
    inspect_env()

if __name__ == "__main__":
    main()