from threading import Thread

class MyThread(Thread):
    """A thread that print its name"""

    def __init(self, name):
        Thread.__init(self, name=name)

    def run(self):
        print("Hello my name is %s" % self.getName())
    
process = MyThread()
print(process.start())