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
