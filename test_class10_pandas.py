import pandas as pd
import pytest


def test_dataframe_shape():
    # This DataFrame has 5 rows and 4 columns.
    df = pd.DataFrame({
        "title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie D"],
        "type": ["Movie", "Movie", "Movie", "Movie", "Movie"],
        "release_year": [2020, 2021, 2022, 2023, 2023],
        "rating": [7, 8, 6, 9, 9],
    })

    # assert checks a condition. If it is true, the test continues. If it is false, the test fails.
    assert df.shape == (5, 4)
    # assert df.shape == (1, 1) 
    # ^ will get an AssertionError
    
# test: python -m pytest -v test_class10_pandas.py

'''
**Arrange** — prepare the input and expected result.
2. **Act** — call the function being tested.
3. **Assert** — compare the actual behavior with the expected behavior.

'''

def test_drop_duplicates():
    # Arrange
    df = pd.DataFrame({
        "title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie D"],
        "type": ["Movie", "Movie", "Movie", "Movie", "Movie"],
        "release_year": [2020, 2021, 2022, 2023, 2023],
        "rating": [7, 8, 6, 9, 9],
    })
    # note: the final two rows are identical, so removing duplicates leaves four rows and four columns.

    # Act
    result = df.drop_duplicates()

    # Assert
    assert result.shape == (4, 4)
    assert result["title"].tolist() == ["Movie A", "Movie B", "Movie C", "Movie D"]


# Part 3: Testing Expected Exceptions
'''
An exception can be the expected result of a test.

`pytest.raises()` checks that a block of code raises the expected exception. For example, `float("unknown")` raises `ValueError`:
'''


with pytest.raises(ValueError):
    float("unknown")

def test_invalid_numeric_value():
    df = pd.DataFrame({"rating": [7, "unknown", 9]})

    with pytest.raises(ValueError):
        pd.to_numeric(df["rating"])


# Part 4: Fixtures
'''
A fixture prepares data or another resource that a test needs. Fixtures reduce repeated setup code when multiple tests need the same data (i.e., we don't want to repeat "pd.DataFrame(...)")

We will use a Python decorator, `@pytest.fixture`, to define fixtures. For example,
'''

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie D"],
        "type": ["Movie", "Movie", "Movie", "Movie", "Movie"],
        "release_year": [2020, 2021, 2022, 2023, 2023],
        "rating": [7, 8, 6, 9, 9],
    })


