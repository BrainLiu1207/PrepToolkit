from psutil import cpu_count
from MultiWrap._base import MPBase
from multiprocessing import Pool
from collections import deque


class PoolRunner(MPBase):
    def __init__(self, 
                 process_func, 
                 input_list, 
                 num_processes=cpu_count(logical=False)-1,
                 to_return=True,
                 ordered=True,
                 **kwargs):
        super.__init__(process_func, input_list, num_processes, to_return, ordered, **kwargs)
        
    def _get_effiective_n(self):
        return min(self.num_processes, len(self.input_list))
    
    def _pool_func(self, input_chunk):
        if self.to_return:
            res = [None] * len(input_chunk)
            for ind, stuff in enumerate(input_chunk):
                res[ind] = self.process_func(stuff)
            return res          
        else:
            for stuff in input_chunk:
                self.process_func(stuff)
                
    def run(self):
        n = self._get_effiective_n()
        
        with Pool(processes=n) as pool:
            if self.to_return and self.ordered:
                result = self._flatten(pool.imap(self._pool_func, self.input_list))
                return result
            else:
                deque(pool.imap_unordered(self._pool_func, self.input_list), maxlen=0)       
        
                