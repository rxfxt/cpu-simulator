import collections

CACHE_SIZE = 32

# This class implements a cache for the CPU
# The deque container datatype is used to mimic FIFO functionality
class Cache:
    def __init__(self):
        self.cache = collections.deque(maxlen = CACHE_SIZE)
        self.flush_cache()

    def flush_cache(self):
        for i in range(CACHE_SIZE):
            self.cache.append(",")

    def write_cache(self, address, value):
        self.cache.append(tuple((address, value)))

    def search_cache(self, address):
        for i in range(CACHE_SIZE):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None
                





    