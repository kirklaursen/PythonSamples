# # Basic example of a decorator function
# You can also use decorator classes
# See https://www.youtube.com/watch?v=FsAPt_9Bf3U


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed here.')
        return original_function()
    return wrapper_function


# def display():
#     print('display function ran\n')

# decorated_display = decorator_function(display)
# # Execute the ordinary display function
# display()

# # Execute the decorated display function
# decorated_display()

# =====================================

# Here is the standard format for decorators
@decorator_function
def display():
    print('display function ran')
# this is equivalent to display = decorator_function(display)

display()

# See loggers.py for a sample use case
