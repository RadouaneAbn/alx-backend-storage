#!/usr/bin/env python3
""" exercice.py """

import redis
from uuid import uuid4
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            This method is to store data in the Redis cache

            Returns:
                id (str): the id of teh new inserted data

        """
        id = str(uuid4())
        self._redis.set(id, data)
        return id
