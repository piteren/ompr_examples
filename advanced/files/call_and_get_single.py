import pickle
from pypaq.lipytools.pylogger import get_pylogger
import subprocess


if __name__ == "__main__":

    logger = get_pylogger(name='builder')

    kwargs = {
        'file_ix':  0,
        'device':   'cpu',
        'save_dir': '_out',
    }

    args = ["python3", "advanced/files/build_file.py"]
    parameters = []
    for k in kwargs:
        parameters += [f'--{k}', str(kwargs[k])]
    res = subprocess.run(
        args=args + parameters,
        capture_output=True,
        check=True,
    )

    arr = pickle.loads(res.stdout)
    print(type(arr), arr.shape)