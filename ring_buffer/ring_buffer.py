class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.counter = 0

    def append(self, item):
        # if storage is less than the max capacity of the buffer
        # append new item to the end of the buffer
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        # if storage is at max capacity
        # check if counter represents a position in storage
        # if counter doesn't represent a position in storage reset counter to 0, counter now represents first position
        # if counter represents a position in storage 
        # make the element at that position equal to the new item
        # increment counter by +1 to represent the next position which will now be the oldest element in storage
        elif len(self.storage) == self.capacity:
            # change to dynamic 
            if self.counter == self.capacity:
                self.counter = 0
            self.storage[self.counter] = item
            self.counter += 1

    def get(self):
        return self.storage