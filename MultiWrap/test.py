from MultiWrap.tqdm_runner import PBarPoolRunner
from MultiWrap.pool_base import PoolRunner
import time
import os
import random

def test_func(x):
    time.sleep(x)
    return x

def f(x):
    time.sleep(x)
    # print(f'pid: {os.getpid()}', flush=True)
    return x


if __name__ == '__main__':
    # runner = PBarPoolRunner(process_func=f,input_list=[1,2,1,1],num_processes=4, ordered=False)
    # runner = PoolRunner(process_func=f,input_list=[1,2,1,1],num_processes=4,to_return=False)
    # generate input list
    input_list = []
    for _ in range(103):
        input_list.append(random.randint(1, 5))
    runner = PBarPoolRunner(process_func=f,input_list=input_list,num_processes=4)
    res = runner.run()
    print(res)
