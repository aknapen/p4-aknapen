class HashEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = [value]

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value.append(value)

    # def __str__(self):
    #     return "(" + self.key + ": " + str(self.value) + ")"


class HashTable:

    def __init__(self, table_size=191):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on.
        If the key is not already in the table, then the key is inserted, and the value is used as the first
        line number in the list of line numbers. If the key is in the table, then the value is appended to that
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        # key = key.lower()
        original_index = self.horner_hash(key)
        if self.hash_table[original_index] == None:
            self.hash_table[original_index] = HashEntry(key, value)
            self.num_items += 1
        else:
            if self.hash_table[original_index].get_key() == key: # same word case
                # if not value in self.hash_table[original_index].get_value():
                #     self.hash_table[original_index].set_value(value)
                if value > self.hash_table[original_index].get_value()[-1]:
                    self.hash_table[original_index].set_value(value)
            elif self.hash_table[original_index].get_key() != key:
                i = 1
                index = original_index
                while self.hash_table[index] is not None and self.hash_table[index].get_key() != key:
                    index = (original_index + i**2) % self.table_size
                    i += 1
                if self.hash_table[index] == None:
                    self.hash_table[index] = HashEntry(key, value)
                    self.num_items += 1
                else:
                    # if value not in self.hash_table[index].get_value():
                    #     self.hash_table[index].set_value(value)
                    if value > self.hash_table[index].get_value()[-1]:
                        self.hash_table[index].set_value(value)
        if self.get_load_factor() > 0.5:
            self.rehash()

    def rehash(self):
        prev_hash = self.hash_table
        self.table_size = 2 * self.table_size + 1
        self.hash_table = [None]*self.table_size
        self.num_items = 0
        for item in prev_hash:
            if item is not None:
                for val in item.get_value():
                    self.insert(item.get_key(), val)

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        # key = key.lower()
        hash_int = 0
        end = min(len(key), 8)
        for i in range(end):
            hash_int += ord(key[i]) * (31**(end-1-i))
        return hash_int % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        # key = key.lower()
        startslot = self.horner_hash(key)
        found = True
        i = 1
        position = startslot
        while self.hash_table[position] is not None:
            if self.hash_table[position].get_key() == key:
                return found
            else:
                position = startslot + i**2
                position = position % self.get_table_size()
            i += 1
        return not found

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None."""
        # key = key.lower()
        startslot = self.horner_hash(key)
        i = 1
        position = startslot
        while self.hash_table[position] is not None:
            if self.hash_table[position].get_key() == key:
                return position
            else:
                position = startslot + i**2
                if position >= self.get_table_size():
                    position = position % self.table_size
                i += 1
        return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        python_list = []
        for i in range(self.get_table_size()):
            if self.hash_table[i] is not None:
                python_list += [self.hash_table[i].get_key()]
        return python_list

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key.
        If key is not in hash table, returns None."""
        # key = key.lower()
        index = self.get_index(key)
        if index != None:
            return self.hash_table[index].get_value()
        return None

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

# ht = HashTable(10)
# # print(ht.horner_hash("c"))
# ht.insert("c", 1)
# print("GET INDEX", ht.get_index("c"), "c")
# # print(ht.horner_hash("m"))
# ht.insert("m", 2)
# # print(ht.get_index("c"))
# print("GET INDEX", ht.get_index("m"), "m")
# ht.insert("w", 3)
# print("GET INDEX", ht.get_index("w"), "w")
# print("NOT IN TABLE", ht.get_index("j"))
