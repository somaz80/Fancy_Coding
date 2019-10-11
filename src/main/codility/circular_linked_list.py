
# Represents the node of list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    CLASS_VARIABLE = 0

    # Declaring head and tail pointer as null
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

        # This function will add the new node at the end of the list.

    def add(self, data):
        new_node = Node(data)
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            # tail will point to new node.
            self.tail.next = new_node
            # New node will become new tail.
            self.tail = new_node
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head

            # Displays all the nodes in the list

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("Nodes of the circular linked list: ")
            # Prints each node by incrementing pointer.
            print(current.data),
            while current.next != self.head:
                current = current.next
                print(current.data)


def get_power(input_number, power_value):
    if power_value <= 1:
        return input_number
    else:
        return input_number * get_power(input_number, power_value - 1)


def sorting_chars_test():
    arr = [['banana', 16], ['guava', 10], ['litchi', 15], ['mango', 17], ['guava', 21], ['litchi', 16], ['plum', 12],
           ['banana', 14], ['orange', 5]]
    print(arr)
    arr.a
    print(arr)


def main():
    # cl = CircularLinkedList()
    # cl.add(3)
    # cl.add(8)
    # cl.add(9)
    # cl.add(7)
    # cl.add(6)
    # cl.display()
   # sorting_chars_test()
    import numpy as np
    arr = np.array([1, 3, 2, 4, 5])
    print(arr.argsort()[-3:][::-1])


    from bs4 import BeautifulSoup

    import requests
    import sys

    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    tr = soup.findChildren("tr")
    tr = iter(tr)
    next(tr)

    for movie in tr:
        title = movie.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    year = movie.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
    rating = movie.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
    row = title + ' - ' + year + ' ' + ' ' + rating

    print(row)


if __name__ == '__main__':
    main()
