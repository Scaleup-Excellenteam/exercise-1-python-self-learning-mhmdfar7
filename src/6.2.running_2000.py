import time

def _time_function(f, *args, **kwargs):
    # My notes:
    # - Helper function that times function execution
    # - Uses perf_counter for most accurate timing
    # - Returns both result and elapsed time
    # - Simple but effective implementation
    # TODO: Maybe add option to disable return value for memory savings?
    start = time.perf_counter()
    result = f(*args, **kwargs)
    return result, time.perf_counter() - start

def running_2000(f, *args, **kwargs):
    # - Main timing function that wraps _time_function
    # - First validates input is callable
    # - Returns just the elapsed time (not result)
    # - Provides detailed error timing on failure
    
    # Input validation
    if not callable(f):
        raise TypeError("First argument must be callable")
    
    try:
        # Time the function execution
        result, elapsed = _time_function(f, *args, **kwargs)
        return elapsed
    except Exception as e:
        # If function fails, time a no-op to get accurate failure timing
        _, elapsed = _time_function(lambda: None)  
        raise RuntimeError(f"Function failed after {elapsed:.6f} seconds") from e

if __name__ == '__main__':
    print("Print:", running_2000(print, "Hello"))  
    print("Zip:", running_2000(zip, [1, 2, 3], [4, 5, 6])) 
    print("Format:", running_2000("Hi {name}".format, name="Bug")) 