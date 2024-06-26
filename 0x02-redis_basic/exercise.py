#!/usr/bin/env python3
""" exercice.py """

import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Wrapper Function """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper Function """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Wrapper Function """
    in_key = method.__qualname__ + ":inputs"
    out_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper Function """
        self._redis.rpush(in_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(out_key, str(res))
        return res

    return wrapper


def replay(method: Callable) -> None:
    """ This function replays the hostory of a function
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for input_, output_ in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, input_.decode('utf-8'),
                                     output_.decode('utf-8')))


class Cache:
    """
    This class use redis to store data.

    Attributes:
        _redis: instance of teh Redis client.
    """
    def __init__(self) -> None:
        """ Initializes The Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            This method is to store data in the Redis cache

            Returns:
                id (str): the id of teh new inserted data

        """
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """ This method returns a data and cast it using fn

            Returns:
                data (str, bytes, int, float): The value of the key
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ This method return a string value of the key
        """
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """ This method return a int value of the key
        """
        return int(self._redis.get(key).decode("utf-8"))
