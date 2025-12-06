from psutil import cpu_count
from itertools import chain
from functools import partial


class MPBase:
    def __init__(self, 
                 process_func, 
                 input_list, 
                 num_processes=cpu_count(logical=False)-1,
                 to_return=True,
                 ordered=True,
                 **kwargs):
        self.process_func = partial(process_func, **kwargs)
        self.input_list = input_list
        self.num_processes = num_processes
        self.to_return = to_return
        self.ordered = ordered
        self.kwargs = kwargs
    
    @staticmethod
    def _flatten(nested_l):
        return list(chain(*nested_l))
    
    def run(self):
        pass
    