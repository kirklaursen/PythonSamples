# see Corey Schafer tutorial on closures at
# https://www.youtube.com/watch?v=swU3c34d2NQ&t=401s
# Also see info on Decorator functions


def outer_function(message):
    def inner_function():       # also called a wrapper function
        print(message)
    return inner_function       # notice there are no parenthesis

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()
