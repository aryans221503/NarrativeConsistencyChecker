import pandas as pd


def load_train_csv(path="data/backstories/train.csv"):
    """
    Loads training data CSV.
    Expected to contain:
    - story / novel reference
    - backstory text
    - label (0 or 1)
    """
    df = pd.read_csv(path)
    return df


def load_test_csv(path="data/backstories/test.csv"):
    """
    Loads test data CSV.
    Expected to contain:
    - story / novel reference
    - backstory text
    (NO label)
    """
    df = pd.read_csv(path)
    return df
