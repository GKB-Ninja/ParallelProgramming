import time
import tracemalloc

def performance(func):
    """
    A decorator that measures execution time and memory usage.
    Statistics are stored as attributes on the wrapper function.
    """
    def wrapper(*args, **kwargs):
        # 1. Increment the call counter
        wrapper.counter += 1
        
        # 2. Start memory tracking
        tracemalloc.start()
        
        # 3. Start timer
        start_time = time.perf_counter()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        # 4. Stop timer and calculate duration
        end_time = time.perf_counter()
        wrapper.total_time += (end_time - start_time)
        
        # 5. Get memory stats (current, peak) and stop tracking
        _, peak = tracemalloc.get_traced_memory()
        wrapper.total_mem += peak
        tracemalloc.stop()
        
        return result

    # Initialize the required attributes on the wrapper function
    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0
    
    return wrapper
