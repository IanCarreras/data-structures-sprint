class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.new = []
        self.counter = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        elif len(self.storage) == self.capacity and self.counter == 0:
            self.new.append(item)
            self.storage.pop(0)
            self.new.extend(self.storage)
            self.storage = self.new
            self.new = []
            self.counter += 1
        elif len(self.storage) == self.capacity and self.counter > 0:
            new = self.storage[:self.counter]
            old = self.storage[self.counter+1:]
            self.new.extend(new)
            self.new.append(item)
            self.new.extend(old)
            self.storage = self.new
            self.new = []
            if self.counter < 5:
                self.counter += 1
            elif self.counter ==  5:
                self.counter = 0

    def get(self):
        print(self.storage)
        return self.storage


buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.append('j')
buffer.append('k')
buffer.append('l')

buffer.get()