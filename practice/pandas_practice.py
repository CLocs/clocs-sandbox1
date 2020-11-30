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

    # Binary opening and closing
    win = 0.3
    win_struct = [True] * int(round(win / dt))
    # Open: remove small intervals
    df['high2'] = ndimage.binary_opening(df['high'], win_struct)
    # Close: close small gaps
    df['high3'] = ndimage.binary_closing(df['high2'], win_struct)

    # Moving average

def moving_average(b: List[bool], win: int):

    pass


if __name__ == '__main__':
    prac_loc()
