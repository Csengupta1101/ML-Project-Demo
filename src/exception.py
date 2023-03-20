'''sys library helps us to manipulate different parts of python runtime environment '''
import sys

def error_message_detail(error,error_detail:sys):
    ''' Anytime any exception / error occurs , this particular function will be called and pushed. This will be my own custom error message'''
    ''' In the line below the variable exc_tb will provide me with specific details about in which file , which line the exception has occured'''
    exc_tb = error_detail.exc_info()
    '''This will access the file name specified , code details taken from exception handling documenatation'''
    file_name = exc_tb.tb_frame.f_code.co_filename
    ''' This will provide specific error message based on locations'''
    error_message = "Error occured in python script name [{0}] , line number [{1}] , error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
        return error_message)

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
