from ompr.simple import simple_process
import pickle
import subprocess


def call_build(**kwargs):
    args = ["python3", "advanced/files/build_file.py"]
    parameters = []
    for k in kwargs:
        parameters += [f'--{k}',str(kwargs[k])]
    res = subprocess.run(
        args=           args + parameters,
        capture_output= True,
        check=          True,
    )
    arr = pickle.loads(res.stdout)
    return arr


if __name__ == "__main__":

    n_files = 20
    n_devices_cpu = 6
    n_devices_gpu = 4

    devices_gpu = [f'CUDA:{i}' for i in range(n_devices_gpu)]

    tasks = [{
        'file_ix':  n,
        'device':   devices_gpu[n % n_devices_gpu],
        #'save_dir': None,
        'save_dir': '_out',
    } for n in range(n_files)] # prepare tasks

    res = simple_process(
        tasks=              tasks,
        function=           call_build,
        num_workers=        n_devices_cpu,
        report_delay=       2,
        loglevel=           20)

    print(f'{len(res)}x {type(res[0])} {res[0].shape}')