import argparse
import numpy as np
import pickle
from pypaq.lipytools.files import prep_folder, w_pickle
import sys
from typing import Optional


def build(file_ix:int, device:str, save_dir:Optional[str]=None):
    arr = np.random.rand(1000,1000)
    for _ in range(100):
        arr += np.random.rand(1000,1000)
    if save_dir:
        prep_folder(save_dir)
        w_pickle(arr, f'{save_dir}/{file_ix:03}.arr')
    return arr


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file_ix", type=int, help="file index")
    parser.add_argument("--device", type=str, help="device")
    parser.add_argument("--save_dir", type=str, help="optionalsave directory")
    args = parser.parse_args()
    arr = build(**vars(args))
    sys.stdout.buffer.write(pickle.dumps(arr))