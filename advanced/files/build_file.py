import argparse
import numpy as np
from pypaq.lipytools.files import w_pickle

SAVE_DIR = '_out'

def build(file_ix:int, device:str):
    print(f'building {file_ix} on device {device}')
    arr = np.random.rand(1000,1000)
    for _ in range(100):
        arr += np.random.rand(1000,1000)
    w_pickle(arr, f'{SAVE_DIR}/{file_ix:03}.arr')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file_ix", type=int, help="file index")
    parser.add_argument("--device", type=str, help="device")
    args = parser.parse_args()
    build(**vars(args))