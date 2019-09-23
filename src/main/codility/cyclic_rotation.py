class BulbNode:
    def __init__(self, next=None, prev=None, key=None, data=None, ttl=20):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.key = key
        self.data = data

    '''
     returns the  json representation of the node
    '''
    def get_node_as_json(self):
        return {'key': self.key, 'data': self.data}


class BulbArray:
    def __init__(self, maximum_capacity=None, expiration_time=None):
        self.start_node = None
        self.maximum_capacity = maximum_capacity
        self.expiration_time = expiration_time

    '''
        Inserts an item to an empty list does not do anything when it is not empty
    '''

    def insert_in_empty_list(self, cache_node_key=None, cache_node_data=None):
        if self.start_node is None:
            cache_node = BulbNode(key=cache_node_key, data=cache_node_data)
            self.start_node = cache_node

    '''
        inserts an cache node at the start of list
    '''

    def insert_at_start(self, cache_node_key=None, cache_node_data=None):
        if self.start_node is None:
            self.insert_in_empty_list(cache_node_key=cache_node_key, cache_node_data=cache_node_data)
            return
        cache_node = BulbNode(key=cache_node_key, data=cache_node_data)
        cache_node.next = self.start_node
        self.start_node.prev = cache_node
        self.start_node = cache_node

    '''
        inserts an cache node item at the end of the list
    '''

    def insert_at_end(self, cache_node_key=None, cache_node_data=None):
        if self.start_node is None:
            cache_node = BulbNode(key=cache_node_key, data=cache_node_data)
            self.start_node = cache_node
            return
        single_node = self.start_node
        while single_node.next is not None:
            single_node = single_node.next
        cache_node = BulbNode(key=cache_node_key, data=cache_node_data)
        single_node.next = cache_node
        cache_node.prev = single_node

    '''
        Takes a key as input and deletes the node if found after traversing
    '''

    def remove_element_by_key(self, key):
        if self.start_node is None:
            print("The list has no element to delete")
            return False
        if self.start_node.next is None:
            if self.start_node.key == key:
                self.start_node = None
                return True
            else:
                print("Cache Node not found")
            return False

        if self.start_node.key == key:
            self.start_node = self.start_node.next
            self.start_node.prev = None
            return True

        a_node = self.start_node
        while a_node.next is not None:
            if a_node.key == key:
                break
            a_node = a_node.next
        if a_node.next is not None:
            a_node.prev.next = a_node.next
            a_node.next.prev = a_node.prev
            return True
        else:
            if a_node.key == key:
                a_node.prev.next = None
                return True
            else:
                print("Cache Node not found")

    '''
      get the list length of double link list
    '''

    def list_length(self):
        "returns the number of list items"

        count = 0
        current_node = self.start_node

        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next

        return count

    '''
     traverse through the elements to print  data
    '''

    def traverse_list(self):
        if self.start_node is None:
            print("CacheList has no element")
            return
        else:
            a_node = self.start_node
            while a_node is not None:
                print(" Node data found : ", a_node.key, a_node.data)
                a_node = a_node.next

    '''
     traverse through the elements to get data as json
    '''

    def get_cache_data_list(self):
        return_data_array = []
        if self.start_node is None:
            print("CacheList has no element")
            return
        else:
            a_node = self.start_node
            while a_node is not None:
                return_data_array.append(a_node.get_node_as_json())
                a_node = a_node.next
        return return_data_array

