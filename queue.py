import time

class Queue:
    """
    A class for storing the raw queue data
    """

    def __init__(self, items=None):
        """
        (None) Initialise the queue class
        """
        # the list of active queue items
        if items is None:
            self.items = []
        else:
            self.items = items

        # main database for all queue items 
        self.database = {}

    def get_num_questions(self, item):
        """
        (int) Returns the number of questions asked corresponding to a 
        student's name in the database
        Parameter:
            item(QueueItem): A queue item (student)
        """
        # get value from the database dictionary
        return self.database.get(item.name)

    def sort_queue(self):
        """
        (None) Sort the Queue list by time and number of questions asked
        """
        # sort the list by time
        self.items = sorted(self.items, key=lambda item: item.time)
        # sort the list by the number of question asked
        self.items = sorted(self.items, key=lambda item: self.get_num_questions(item))

    def get_items(self):
        """
        (QueueItem) Returns the queue items currently in the active queue class
        """
        return self.items

    def get_avg_wait_time(self):
        """
        (float) Returns the calculated average wait time
        """
        total = 0
        for start_time in [item.time for item in self.items]:
            timestamp = time.time() - start_time
            total += timestamp
        # the total time divided by the number of students in the active queue
        avg_time = total / len(self.items)
        return avg_time

    def add_item(self, item, other):
        """
        (bool) Add a queue item to the queue list and returns 
        True or False when added or not added successfully
        Parameter:
            item(QueueItem): A queue item to be added
            other(Queue): another Queue to be compared with
        """
        # check if name already exists in both current queues
        if item.name not in [item.name for item in self.items] and item.name not in [item.name for item in other.items]:
            # if data not already in database, add to both current queue and database
            if item.name not in self.database:
                self.items.append(item)
                # initialise the number of question asked to be 0 
                self.database.update({item.name: 0})
                # sort queue after adding item
                self.sort_queue()
            elif item.name in self.database:
                # only add the student to current queue if already in the database
                self.items.append(item)
                self.sort_queue()
            return True
        else:
            return False

    def remove_item(self, name):
        """
        (None) Remove a given item name from the Queue list
        Parameter:
            name(str): student's name to be removed
        """
        self.items = [item for item in self.items if item.name != name]

    def __str__(self):
        """
        (str) Returns a string representation of the queue object
        """
        s = "Our students queue contains\n"
        for i, item in enumerate(self.items):
            item = self.items[i]
            s += f"[{i}] {item} {self.database.get(item.name)}\n"
        return s


class QueueItem:
    """
    A class which represents queue items
    """
    def __init__(self, name):
        """
        (None) Initialise the queue item class
        Parameter:
            name(str): a queue item's name
        """
        self.name = name
        self.time = time.time()

    def __str__(self):
        """
        (str) Returns a string representation of the queue item
        """
        return f" NAME: {self.name}          | TIME: {self.time}    "

    def get_item_name(self):
        """
        (str) Returns the queue item's name
        """
        return self.name