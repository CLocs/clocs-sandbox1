import pandas as pd
import numpy as np
from typing import List
from scipy import ndimage


def prac_loc():
    # make some df
    n = 50
    l = np.random.randn(n)
    df = pd.DataFrame({
        't': [0.1 * i for i in range(0, n)],
        'rand': l
    })
    df2 = df.loc[df['rand'] > 0.6]
    df2 = df.loc[(df['rand'] > 0.6) & (df['rand'] < 0.8)]

    df['high'] = df['rand'] > -0.2

    dt = np.mean(np.diff(df['t']))

    win = 0.3
    win_struct = [True] * int(round(win / dt))
    df['high2'] = ndimage.binary_opening(df['high'], win_struct)
    win = 0.3
    win_struct = [True] * int(round(win / dt))
    df['high3'] = ndimage.binary_closing(df['high2'], win_struct)
    billy = 1


if __name__ == '__main__':
    prac_loc()
