import logging

logger = logging.getLogger(__name__)

def show_overview(df):
    """Display basic information about a DataFrame."""
    logger.DEBUG(f"Overview shape: {df.shape}")
    print(df.shape, df.head(), (count(df.columns)), df.dtypes)

def remove_duplicates(df):
    """Remove exact duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    logger.debug(f"Started with {before} rows and removed {before - len(df)} duplicate row(s)")
    return df

def drop_missing_rows(df):
    """Remove rows containing missing values."""
    rows_dropped = df.dropna()
    logger.debug(f" Started with {len(df)} rows and now has {(len(df))- (rows_dropped)}")
    return df
