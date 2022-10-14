syntax errors
   As the name suggests this error is caused by the wrong syntax in the code.
It leads to the termination of the program. 



exceptions:
    Exceptions are raised when the program is syntactically correct,
    but the code resulted in an error.
    This error does not stop the execution of the program, however,
    it changes the normal flow of the program.
    
        1,zero divison error
        2,name error
        3,type_error
handling exceptions:
          _try
          catch

rasising exception:
    The raise statement allows the programmer to force a specific exception to occur.
    The sole argument in raise indicates the exception to be raised.
    This must be either an exception instance or an exception class (#a class that derives from Exception).
          _raise

exception chaining:
          _raise
          _from

user defined exception:

defining clean up actions:

predefined clean up actions:


          
    Exception                                Description
          
ArithmeticError    	Raised when an error occurs in numeric calculations
AssertionError	        Raised when an assert statement fails
AttributeError	        Raised when attribute reference or assignment fails
Exception	        Base class for all exceptions
EOFError	        Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError	Raised when a floating point calculation fails
GeneratorExit	        Raised when a generator is closed (with the close() method)
ImportError	        Raised when an imported module does not exist
IndentationError	Raised when indendation is not correct
IndexError	        Raised when an index of a sequence does not exist
KeyError	        Raised when a key does not exist in a dictionary
KeyboardInterrupt	Raised when the user presses Ctrl+c, Ctrl+z or Delete
LookupError	        Raised when errors raised cant be found
MemoryError	        Raised when a program runs out of memory
NameError	        Raised when a variable does not exist
NotImplementedError	Raised when an abstract method requires an inherited class to override the method
OSError	                Raised when a system related operation causes an error
OverflowError   	Raised when the result of a numeric calculation is too large
ReferenceError  	Raised when a weak reference object does not exist
RuntimeError	        Raised when an error occurs that do not belong to any specific expections
StopIteration   	Raised when the next() method of an iterator has no further values
SyntaxError	        Raised when a syntax error occurs
TabError	        Raised when indentation consists of tabs or spaces
SystemError	        Raised when a system error occurs
SystemExit	        Raised when the sys.exit() function is called
TypeError	        Raised when two different types are combined
UnboundLocalError	Raised when a local variable is referenced before assignment
UnicodeError	        Raised when a unicode problem occurs
UnicodeEncodeError	Raised when a unicode encoding problem occurs
UnicodeDecodeError	Raised when a unicode decoding problem occurs
UnicodeTranslateError	Raised when a unicode translation problem occurs
ValueError	        Raised when there is a wrong value in a specified data type
ZeroDivisionError	Raised when the second operator in a division is zero
