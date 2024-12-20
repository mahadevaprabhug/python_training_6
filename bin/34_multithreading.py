"""
multithreading
"""
print("WITHOUT using multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("USING multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]

from threading import Thread

my_thread_1 = Thread(target=my_square_function, args=[L])
my_thread_2 = Thread(target=my_cube_function, args=[L])

my_thread_1.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

my_thread_2.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

# Wait here till both threads completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]
my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("WITH DELAY: USING multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

from threading import Thread

my_thread_1 = Thread(target=my_square_function, args=[L])
my_thread_2 = Thread(target=my_cube_function, args=[L])

my_thread_1.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

my_thread_2.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

# Wait here till both threads completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("USING LOCKING multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()

from threading import Lock
my_lock = Lock()
def my_square_function(my_list):
    my_lock.acquire()
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)
    my_lock.release()



L = [10, 20, 30, 40, 50]

from threading import Thread

my_thread_1 = Thread(target=my_square_function, args=[L])
my_thread_2 = Thread(target=my_square_function, args=[L])

my_thread_1.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

my_thread_2.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

# Wait here till both threads completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("OVERRIDING THREAD CLASS: multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

from threading import Thread


class MyThreadClass(Thread):
    def __init__(self, my_thread_name, my_function_name, input_list):
        Thread.__init__(self) # Calling super class init
        self.my_thread_name = my_thread_name
        self.my_function_name = my_function_name
        self.input_list = input_list

    def run(self):
        print("Start of run method")
        print("Currently Executing Thread:", self.my_thread_name)
        self.my_function_name(self.input_list)
        print("Thread Execution Completed")
        print("End of run method")


my_thread_1 = MyThreadClass("my_thread_1", my_square_function, L)
my_thread_2 = MyThreadClass("my_thread_2", my_cube_function, L)

# my_thread_1 = Thread(target=my_square_function, args=[L])
# my_thread_2 = Thread(target=my_cube_function, args=[L])

my_thread_1.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

my_thread_2.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

# Wait here till both threads completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################

print("WITH LOCK: OVERRIDING THREAD CLASS: multithreading")
print("-"*20)
# --------------
import time

start_time = time.time()
def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

from threading import Thread

from threading import Lock
my_lock = Lock()

class MyThreadClass(Thread):
    def __init__(self, my_thread_name, my_function_name, input_list):
        Thread.__init__(self) # Calling super class init
        self.my_thread_name = my_thread_name
        self.my_function_name = my_function_name
        self.input_list = input_list

    def run(self):
        my_lock.acquire()
        print("\nStart of run method")
        print("Lock aquired by the thread:", self.my_thread_name)
        print("Currently Executing Thread:", self.my_thread_name)
        self.my_function_name(self.input_list)
        print("Thread Execution Completed")
        print("End of run method")
        print("Lock Released\n")
        my_lock.release()

my_thread_1 = MyThreadClass("my_thread_1", my_square_function, L)
my_thread_2 = MyThreadClass("my_thread_2", my_cube_function, L)

# my_thread_1 = Thread(target=my_square_function, args=[L])
# my_thread_2 = Thread(target=my_cube_function, args=[L])

my_thread_1.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

my_thread_2.start()
# this will start the thread and goto next line. Which means it will not wait for
# thread execution to complete

# Wait here till both threads completes execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()

print("Time Taken:", end_time-start_time)
print("Time Taken (roundup):", round(end_time-start_time, 3))

print("#"*40, end="\n\n")
################################
