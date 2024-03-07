""" 1. This is a decorator to log the following details whenever a function is called
# 	a. The name of the File is <module>_<YYYYMMDD>.log
# 	b. The messages in the logs file is in the format as below
# 		<module name> <function name> <DD-MM-YY> <hh:mm:ss> <Dict of Arguments passed to the function>
"""

import datetime
import time

def log_decorator(func):
    """function that logs the details"""

    def wrapper(*args, **kwargs):
        """wrapper function for logging"""
        date = datetime.datetime.now()
        module_name = func.__module__
        function_name = func.__name__
        formatted_date = date.strftime("%d-%m-%y")
        curr_time = date.strftime("%H:%M:%S")
        start_time = time.time()

        #Extract arguments passed to the function
        args_dict = {}
        if args:
            args_dict['args'] = args
        if kwargs:
            args_dict['kwargs'] = kwargs

        # Call the original function
        result = func( *args, **kwargs)
        execution_time = time.time()-start_time

        # Log details to file
        log_file_name = f"{module_name}_{date.strftime('%Y%m%d')}.log"
        log_file_message = f"{module_name} {function_name} {formatted_date} {curr_time} {args_dict} Execution time: {execution_time:.4f} seconds"

        with open(log_file_name, 'a', encoding="utf-8") as log_file:
            log_file.write(log_file_message + "\n")

        return result

    return wrapper
