from threading import Thread, current_thread
import time, random

class SharedCell(object):
    def __init__(self):
        """Data undefind at startup"""
        self.data = -1
    
    def set_data(self, data):
        """Producer's menthod to write to shared data."""
        print("%s setting data to %d" %\
              (current_thread().getName(), self.data))
        return self.data
    
    def get_data(self):
        """Consumer's method to read from shared data."""
        print("%s accessing data %d" %  
              (current_thread().getName(), self.data))
        return self.data
    
class Producer(Thread):
    """Producer of data in a shell cell."""
    def __init__(self, cell, access_count, sleep_max):
        """Create a producer with the given shared cell,
        number of acesses, and maximum sleep interval. 
        """
        Thread.__init__(self, name= "Producer")
        self.access_count = access_count
        self.cell = cell
        self.sleep_max = sleep_max

    def run(self):
        """Annouce start-up, sleep and write to shared cell the 
        given number of times, and annouce completion."""
        print("%s starting up " % self.getName())
        for count in range(self.access_count):
            time.sleep(random.randint(1, self.sleep_max))
            self.cell.set_data(count+1)
        print("%s is done produceing\n" % self.getName())

class Consumer(Thread):
    """Consumer of data in a shared cell."""

    def __init__(self, cell, access_count, sleep_max):
        """Creates a consumer with the given shared cell number
        of accesses and maximum sleeep interval."""
        Thread.__init__(self, name = Consumer)
        self.access_count = access_count
        self.cell = cell
        self.sleep_max = sleep_max
        
    def run(self):
        """Annouce start-up, sleep and read fron shared cell the
        given number of times, and annouce completion"""
        print("%s starting up " % self.getName())
        for count in range(self.access_count):
            time.sleep(random.randint(1, self.sleep_max))
            Value = self.cell.get_data()
        print("%s is done consuming\n " % self.getName())




class MyThread(Thread):
    """A thread that print its name"""

    def __init(self, name):
        Thread.__init(self, name=name)

    def run(self):
        print("Hello my name is %s" % self.getName())
    
process = MyThread()
print(process.start())