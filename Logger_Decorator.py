# For  more info about decorators, see
#       https://www.youtube.com/watch?v=FsAPt_9Bf3U
# For more info about logging, see
#       https://www.youtube.com/watch?v=-ARI4Cz-awo&list=PL-osiE80TeTv5x_nJb-mtaEKg9Gi_-Nsh&index=1
#       https://www.youtube.com/watch?v=jxmzY9soFXg&list=PL-osiE80TeTv5x_nJb-mtaEKg9Gi_-Nsh&index=2

from functools import wraps


def my_logger(orig_func):
    import logging
    # this logging setup sends logs to a file named after the function
    # logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    # this logging setup just sends logs to the console
    logging.basicConfig(level=logging.INFO)

    @wraps(orig_func)   # needed to preserve the original function name
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print('{} is {} years old.'.format(name, age))

display_info('John', 23)
display_info('Amy', 26)
