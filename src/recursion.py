# understanding call stack

# if you slow computer down it is only ever doing one thing at a time
    # if you have multiple functions


# def foo():
#     print("function 1")
#     return

# def bar():
#     print("function 2")
#     return

# def baz():
#     foo()
#     bar()
#     return

# print(baz())

# the python environemnt is always running a function called python 3 in the background
# everytime a function is invoked python3 pauses whatever it is doing and runs the function invoked
# when a function is invoked it gets put on the call stack
# when a function contains "return" this tells the function to be removed from the call stack 

# print enters the stack - print pauses
    # baz enters the stack - baz pauses
        # foo enters the stack
            # foo returns - exits the stack
        # bar enters the stack
            # bar returns - exits the stack
        # baz resumes - returns - exits the stack
    # print resumes and has completed - exits the stack

#FIBONACCI
    # to arrive at a specific index n just add the 2 previous numbers together
    # fib(n) = fib(n - 1) + fib(n - 2)

def fib(n):
    # the base case
    if n <= 1:
        return n
    # the recursive case
    else:    
        return fib(n-1) + fib(n-2)

print(fib(0))
print(fib(1))
print(fib(2))

# understanding the base case
# what input is going to lead us to the condition which determines termination of the function

# the recrusive case
# needs to define the behavior that leads toward the condition of the base case
