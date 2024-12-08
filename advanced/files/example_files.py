from ompr.simple import simple_process
from pypaq.lipytools.files import prep_folder
import subprocess

from build_file import SAVE_DIR


def call_build(**kwargs):
    #print(f'will call with kwargs {kwargs}')
    args = ["python3", "advanced/files/build_file.py"]
    parameters = []
    for k in kwargs:
        parameters += [f'--{k}',str(kwargs[k])]
    subprocess.run(
        args=   args + parameters,
        check=  True,
    )


if __name__ == "__main__":

    n_files = 20
    n_devices_cpu = 6
    n_devices_gpu = 4

    devices_gpu = [f'CUDA:{i}' for i in range(n_devices_gpu)]
    prep_folder(SAVE_DIR)

    tasks = [{'file_ix':n, 'device':devices_gpu[n % n_devices_gpu]} for n in range(n_files)] # prepare tasks
    print(tasks)

    # process tasks and get results
    res = simple_process(
        tasks=              tasks,
        function=           call_build,
        num_workers=        n_devices_cpu,
        #rww_init_sync=      True,
        #rerun_crashed=      False,
        #log_rww_exception=  False,
        report_delay=       2,
        loglevel=           20)

    print(len(res))