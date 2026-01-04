from tqdm import tqdm
from MultiWrap.pool_base import PoolRunner
from MultiWrap.utils import split
from multiprocessing import Pool
from psutil import cpu_count


class PBarPoolRunner(PoolRunner):
    def __init__(self, 
                 process_func, 
                 input_list, 
                 num_processes=cpu_count(logical=False)-1,
                 to_return=True,
                 ordered=True,
                 **kwargs):
        super().__init__(process_func, input_list, num_processes, to_return, ordered, **kwargs)
        
    def run(self):
        effective_n = self._get_effiective_n()
        chunks = split(self.input_list, n=effective_n*100)
        result = [None] * len(self.input_list)
        with tqdm(total=len(self.input_list)) as pbar:
        
            with Pool(processes=effective_n) as pool:
                if self.ordered:
                    start_ind = 0
                    for chunk in pool.imap(self._pool_func, chunks):
                        end_ind = start_ind + len(chunk)
                        result[start_ind: end_ind] = chunk
                        start_ind += len(chunk)
                        pbar.update(n=len(chunk)) 
                    return result
                else:
                    for chunk in pool.imap_unordered(self._pool_func, chunks):
                        pbar.update(n=len(chunk))
        
        
        