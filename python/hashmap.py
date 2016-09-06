# Implementation of the Map ADT using closed hashing and a probe with double hashing.
from arrays import Array

class HashMap:
    # Defines constants to represent the status of each table entry
    UNUSE = None
    EMPTY = _MapEntry( None, None)

    # Creates an empty map instance.
    def __init__( self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - (len(self._table) // 3)

    # Returns the number of entries in the map.
    def __len__(self):
        return self._count

    # Determines if the map contains the given key.
    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None




    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.
    def _findSlot(self, key, forInsert):
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)






    # The main hash function for mapping keys to table entries.
    def _hash1(self, key):
        # we use hash(). so the key have to be hashable key.j
        return abs(hash(key)) % len(self._table)

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)




# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__( self, key, value):
        self.key = key
        self.value = value


