import time
from functools import wraps


def decorate(limit_time, count):
    def wrapper(func):
        time_list = []

        def inner_wrapper(*args, **kwargs):
            now_time = time.time()
            if len(time_list) == count:
                if now_time - time_list[0] >= limit_time:
                    time_list.pop(0)
                    time_list.append(now_time)
                    func(*args, **kwargs)
                else:
                    print 'fuck'
            else:
                time_list.append(now_time)
                return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@decorate(1, 3)
def say(something):
    return something


if __name__ == '__main__':
    a = say

    for _ in range(11):
        say('Done')
    time.sleep(3)
    for _ in range(11):
        say('Done')
