import argparse
import numpy as np
import pickle
from pypaq.lipytools.files import prep_folder, w_pickle
import sys
from typing import Optional


def build(
        file_ix: int,
        device: str, # this is the way to pass GPU device
        save_dir: Optional[str]=    None,
        dim: int=                   2000):
    arr = np.random.rand(dim,dim)
    if save_dir:
        prep_folder(save_dir)
        w_pickle(
            obj=        arr,
            file_path=  f'{save_dir}/{file_ix:03}_{device}.arr',
            compressed= True)
    return arr


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file_ix", type=int, help="file index")
    parser.add_argument("--device", type=str, help="device")
    parser.add_argument("--save_dir", type=str, help="optional save directory")
    args = parser.parse_args()
    arr = build(**vars(args))
    sys.stdout.buffer.write(pickle.dumps(arr))