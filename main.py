import time, random
from producer_consumer import SharedCell, Producer, Consumer

def main():
    """Get the number of accessses from the user, creat a 
    shared cell, and create and start up a producer and a consumer"""
    access_count = int(input("enter the number of accesses: "))
    sleep_max = 4 
    cell = SharedCell()
    producer = Producer(cell, access_count, sleep_max)
    consumer = Consumer(cell, access_count, sleep_max)

    print("Starting the threads")
    producer.start()
    consumer.start()

 
if __name__== "__main__":
    main()