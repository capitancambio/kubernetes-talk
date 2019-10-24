import pandas as pd
from scripts.transform import _important_op


def test_important_op():
    df = pd.DataFrame({"values": [1, 2, 3]})
    result = _important_op(df)
    assert pd.np.all(result.values.flatten() == pd.np.array([2, 4, 6]))
