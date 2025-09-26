"""
7) Decorators Task
   - Create a decorator called "log_time" that:
        - Records the execution time of any function.
        - Saves the function name and runtime into "execution_log.txt".
   - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
   - Verify that the log file contains entries after running.

"""
import time
from functools import wraps


def log_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        elapsed=end-start

        log_file="execution_log.txt"
        with open(log_file,"a") as f:
            f.write(f"{func.__name__} excuted in {elapsed:.4f} seconds \n")
        return result
    return wrapper()