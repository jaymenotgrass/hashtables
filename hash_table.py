class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * self.size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        # If index is empty, insert directly
        if self.data[index] is None:
            self.data[index] = new_node
            return

        # Otherwise, traverse linked list for collision handling
        current = self.data[index]
        prev = None
        while current:
            # If key already exists, update the number
            if current.key == key:
                current.value.number = number
                return
            prev = current
            current = current.next

        # Add new node to the end of the chain
        prev.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        # Traverse chain at that index
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Not found

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()  # Newline for next index

# Test your hash table implementation here.  

table = HashTable(10)
table.print_table()

# Add some values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()

# Search for a value
contact = table.search("John") 
print("\nSearch result:", contact)

# Edge Case #1 - Hash Collisons (assuming these hash to the same index) 
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()

# Edge Case #2 - Duplicate Keys 
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris"))

## A. Why is a hash table the right structure for fast lookups?
#       Since a hash table uses a special calculation that takes a key and 
#       converts it into a number, which becomes the index that can be stored and 
#       looked up. With this method, it can be fast to lookup values because it 
#       just goes directly to the value instead of searching through each item. 

## B. How did you handle collisions?
#       I handled collisions by creating each position to have separate chaining. 
#       This means that each node holds a separate linked list and once their is a 
#       collision that occurs, we linked them together in the same index. 

## C. When might an engineer choose a hash table over a list or tree?
#       Like learned before, hash tables are used for fast lookups. They aren't 
#       used if order is necessary or if their are duplicates. So, when an engineer
#        might need to use this is when they are growing through data or insertions 
#        that needs to be fast. For specific examples, if an engineer is needing to 
#       find a contact name for a certain employee or if they are checking if a 
#       username exists in the right customer value, they would use a hash table. 
#       The engineers would also use this method if all of the keys would be unique.
#       Most usernames for customers should all be different, creating this unique 
#       attribute. Like said before, order is not important within hash tables so 
#       if they don't need to preserve order, they would use this method. 