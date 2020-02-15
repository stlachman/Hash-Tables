# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if not self.storage[self._hash_mod(key)]:
          self.storage[self._hash_mod(key)] = LinkedPair(key, value)
        else:
          node = LinkedPair(key, value)
          node.next = self.storage[self._hash_mod(key)]
          self.storage[self._hash_mod(key)] = node



    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        if not self.storage[self._hash_mod(key)]:
          print("No value here.")
        else:
          head = self.storage[self._hash_mod(key)] 
          if not head.next:
            self.storage[self._hash_mod(key)] = None
          # next value so we know that we are dealing with a linked list
          else:
            if head.key == key:
              self.storage[self._hash_mod(key)] = head.next
            else: 
              prev = head
              current = prev.next 
              while current: 
                if current.key == key:
                  prev.next = current.next
                current = current.next


    def retrieve(self, key):
        if not self.storage[self._hash_mod(key)]:
          return None
        else:
          current = self.storage[self._hash_mod(key)]  
          while current: 
            if current.key == key:
              return current.value
            current = current.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        new_hash = HashTable(self.capacity * 2)
        for node in self.storage:
          if node:
            current = node 
            while current:
              new_hash.insert(current.key, current.value)
              current = current.next
        self.storage = new_hash.storage
        self.capacity = new_hash.capacity



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
