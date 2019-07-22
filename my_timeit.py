import time

def timeit(fun):
    def timed(*args, **kw):
        ts = time.time()
        result = fun(*args, **kw)
        te = time.time()
        
        elapsed = te - ts
        print(f"Elapsed time is {elapsed:6.2f}s")
        
        return result
    
    return timed