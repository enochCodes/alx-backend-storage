#!/usr/bin/env python3
"""
Cache class to store data in Redis
"""
import redis
import uuid
from typing import Union

class Cache:
    def __init__(self) -> None:
        # Define _redis as an instance variable
        self._redis = redis.Redis(decode_responses=True)
        # Flush the Redis database
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key
        key = str(uuid.uuid4())
        # Store the data in Redis with the generated key
        self._redis.set(key, data)
        # Return the key as a string
        return key

