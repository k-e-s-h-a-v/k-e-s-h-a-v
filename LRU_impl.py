class LRUCache(object):
    def __init__(self, memory_space):
        self.memory_space = memory_space
        self.cache = {}
        self.oldest_to_latest = []
        print(f"cache of size {memory_space} created")

    def get(self, key):
        if key not in self.cache:
            return -1

        self.oldest_to_latest.remove(key)
        self.oldest_to_latest.append(key)

        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.oldest_to_latest.remove(key)
        elif len(self.cache) == self.memory_space:
            lru = self.oldest_to_latest.pop(0)
            del self.cache[lru]

        self.cache[key] = value
        self.oldest_to_latest.append(key)
        return None
        

command_seq = ["LRU", "PUT", "GET", "GET", "PUT"]

ref = [[2], [1, 1], [1], [2], [2, 2]]

lru_cache = None

for command, values in zip(command_seq, ref):
    if command == "LRU":
        lru_cache = LRUCache(values[0])
    elif command == "PUT":
        print(lru_cache.put(values[0], values[1]))
    elif command == "GET":
        print(lru_cache.get(values[0]))
