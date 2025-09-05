class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value

    def set(self, key):
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) >= limit:
                del self.cache[next(iter(self.cache))]
            self.cache[key] = value
            


if __name__ == "__main__":
    pass
