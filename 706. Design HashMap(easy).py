class MyHashMap(object):

    def __init__(self):
        self.size = 1000000
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def put(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))
        

    def get(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break


        if found_key:
            return record_val
        else:
            return -1
        

    def remove(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return