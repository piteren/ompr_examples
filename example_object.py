import random
import time

from ompr.runner import RunningWorker, OMPRunner


class Processor(RunningWorker):
    """ processes given task """

    def __init__(self, factor:float):
        super().__init__()
        time.sleep(10)
        self.factor = factor

    def process(self, a:float, b:float) -> float:
        time.sleep(1)
        return a * b * self.factor


if __name__ == "__main__":

    tasks = [{'a':random.random(), 'b':random.random()} for _ in range(100)]

    ompr = OMPRunner(
        rww_class=          Processor,
        rww_init_kwargs=    {'factor': 0.7},
        devices=            0.5,        # uses half of system CPUs
        #devices=            [None]*10,  # uses 10 CPUs
        report_delay=       5,
        loglevel=           10)

    ompr.process(tasks)
    res = ompr.get_all_results()
    ompr.exit()

    print(len(res))
    print(res)