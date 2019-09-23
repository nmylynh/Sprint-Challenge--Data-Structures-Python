# buffer: store (data) in a buffer while it is being processed or transferred.
# A ring buffer is a buffer with a fixed size. When it fills up, adding another element overwrites the oldest one that was still being kept. It’s particularly useful for the storage of log information and history. 

# Buffer research link: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity # initialize storage

  def append(self, item):
    self.storage[self.current] = item # set item into storage
    if self.current < self.capacity - 1: # if less than max capacity (-1 for list assignment index)
      self.current += 1 # increment current
    else:
      self.current = 0 # if max capacity reset to 0

  def get(self):
    return [item for item in self.storage if item != None]