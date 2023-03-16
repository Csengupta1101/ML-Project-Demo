'''sys library helps us to manipulate different parts of python runtime environment '''
import sys

def error_message_detail(error,error_detail):
    ''' Anytime any exception / error occurs , this particular function will be called and pushed. This will be my own custom error message'''
    ''' In the line below the variable exc_tb will provide me with specific details about in which file , which line the exception has occured'''
    exc_tb = error_detail.exc_info()
    error_message_detail

