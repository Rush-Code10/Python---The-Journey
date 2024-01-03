def longtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@longtime
def hello():
    print("Hello")

hello()

"""
A decorator is a design pattern in Python that allows you to modify the behavior of a function or a class without 
changing its source code. A decorator is essentially a callable that takes another function as an argument, 
performs some action on the input function, and returns the modified function as output.

In Python, you can define a decorator function using the "@" symbol followed by the name of the decorator function. 
You can then apply the decorator to the target function or class by placing the decorator symbol above its definition.
 When the decorated function or class is called, the decorator function intercepts the call and executes some 
 additional code before and/or after the target function is executed.

Decorators are a powerful feature of Python that can be used for a variety of purposes, such as:

Adding logging, profiling, or debugging functionality to a function
Implementing caching or memoization of function results to speed up computations
Adding authentication, authorization, or rate-limiting checks to a function
Implementing decorators to validate inputs to a function or sanitize its output
Implementing a decorator to time function execution
Implementing decorators to add error-handling and exception-catching code around a function call.
Decorators help to keep code clean and readable by separating concerns and promoting code reuse. They allow you to add functionality to existing functions or classes without cluttering their source code with additional logic or dependencies.
"""
'''
This is an example of a decorator function called "longtime". 
The decorator "longtime" wraps around the function "hello" and adds some additional functionality to it.
The "longtime" decorator defines a new function called "wrapper" which is returned instead of the original function. 
The "wrapper" function executes the original function and adds some additional code before and after it.
When the decorated function "hello" is called, it actually calls the "wrapper" function defined by the decorator. 
The "wrapper" function first prints "before", then calls the original function "hello" which prints "Hello", 
and then prints "after". Finally, it returns the value returned by the original function.
'''