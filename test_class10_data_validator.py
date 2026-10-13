import pandas as pd
import pytest

from class10_data_validator import validate_columns

@pytest.fixture
def sample_df():
    """Create a small DataFrame for testing."""
    return pd.DataFrame(
        {
            "title": ["Movie A", "Movie B"],
            "type": ["Movie", "Movie"],
            "release_year": [2020, 2021],
        }
    )

def test_validate_columns_with_valid_columns(sample_df):
    # TODO 1:
    required_columns = ["title", "type", "release_year"]
    result = validate_columns(sample_df, required_columns)
    assert list(result.columns) == required_columns
    assert result.shape == (2, 3)
    assert df.columns.tolist() == required_columns
    


def test_validate_columns_with_missing_column(sample_df):
    required_columns = ["rating"]

    with pytest.raises(ValueError):
        validate_columns(sample_df, required_columns)


'''
## Requirements

Your tests should confirm that:

1. `validate_columns()` returns a DataFrame with the expected columns when all required columns exist.
2. `validate_columns()` raises `ValueError` when `rating` is required but missing.
3. The exception test checks that the message contains `Missing required columns`.
4. Both tests use the `sample_df` fixture.

'''