import sys
import logging
# This sys library handles the python runtime environment i.e. any exception occured while running the code will go to the sys module.

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = sys.exc_info()
    # This "sys.exc_info()" returns a tuple of 3 params first is the exception type which denotes the type of exception being handled e.g. <class 'ZeroDivisionError'>, second one is the exception value which gets the instance of an exception type i.e. the error message e.g. ZeroDivisionError('division by zero') & the last one is the exception traceback(i.e. exc_tb) which returns a traceback object that encapsulates the system call stack at the point where the exception originated.

    # The filename, line no. & the error msg of the exception can be found out using below 3 lines of code...
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    err = str(error)

    error_msg = f"Error occured in the python script named {filename}, in the line no. {lineno} & the error message is {err}"
    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_message_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg
