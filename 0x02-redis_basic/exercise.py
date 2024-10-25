#!/usr/bin/env python3
"""
Cache class to store data in Redis
with support for type conversion on retrieval.
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    def __init__(self) -> None:
        # Initialize Redis client and flush database
        self._redis = redis.Redis(decode_responses=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a random key and returns the key."""
        key = str(uuid.uuid4())  # Generate a unique key as a string
        self._redis.set(key, data)
        return key

    def get(self,
            key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """Retrieves data from Redis,
        optionally applying a conversion function."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)  # Apply the conversion function if provided
        return data  # Return data as-is if no conversion function is provided

    def get_str(self, key: str) -> str:
        """Retrieves data from Redis and converts it to a UTF-8 string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves data from Redis and converts it to an integer."""
        return self.get(key, fn=int)
