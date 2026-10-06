import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    drop_missing_rows,
    remove_duplicates,
    show_overview,
)

logger = logging.getLogger(__name__)


def main():

    # p = Path(args.input)
    # try:
    #     pd.read_csv(p)
    # except FileNotFoundError:
    #     logger.ERROR(f"File not found: '{args.input}'")
    #     sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    p = Path(args.input)
    try:
        pd.read_csv(p)
    except FileNotFoundError:
        logger.ERROR(f"File not found: '{args.input}'")
        sys.exit(1)

    logger.info(f"Loaded Netflix data from '{args.input}'")
    df=pd.read_csv(p)
    show_overview(df)
    logger.info("Logged info about data")

    # TODO 6:
    # Call remove_duplicates().
    # Call drop_missing_rows().
    # Log an INFO message after each step that
    # includes the number of rows removed.

if __name__ == "__main__":
    main()