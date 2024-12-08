from ompr.simple import simple_process
import random
import time


# function processing tasks
def func(a:float, b:float) -> float:
    if random.random() > 0.5:
        raise Exception('RandomException')
    #if random.random() > 0.5:
    #    raise KeyboardInterrupt
    time.sleep(0.5)
    return a*b


if __name__ == "__main__":

    tasks = [{'a':random.random(), 'b':random.random()} for _ in range(100)] # prepare tasks

    # process tasks and get results
    res = simple_process(
        tasks=              tasks,
        function=           func,
        num_workers=        4,
        #rww_init_sync=      True,
        #rerun_crashed=      False,
        #log_rww_exception=  False,
        report_delay=       2,
        loglevel=           10)

    print(len(res))
    print(res)