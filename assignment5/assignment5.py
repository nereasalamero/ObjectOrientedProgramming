# **********************************************
# Title:        Asignments 5
# Author:       Nerea Salamero Labara
# Date:         09/02/2025
# File:         assignment5.py
# Subject:      Object Oriented Programming
# Description:  
# **********************************************
import time


# Assignment 5:
# Implement a Stopwatch class with private attributes and methods like start(), stop(), reset(), and elapsed_time().
# Define all the attributes as private.
class Stopwatch:
    def __init__(self):
        self.__start_time = None
        self.__elapsed_time = 0.0
        self.__running = False

    def start(self):
        if not self.__running:
            self.__start_time = time.time()
            self.__running = True

    def stop(self):
        if self.__running and self.__start_time is not None:
            self.elapsed_time += time.time() - self._start_time
            self.__start_time = None
            self.__running = False

    def reset(self):
        self.__start_time = None
        self.__elapsed_time = 0.0
        self.__end_time = None

    def elapsed_time(self):
        if self.__running and self.__start_time is not None:
            return self.__elapsed_time + (time.time() - self.__start_time)
        return self.__elapsed_time

sw = Stopwatch()
i = 0
sw.start()
while i < 5:
    time.sleep(1)
    print(f"Elapsed time: {sw.elapsed_time()}")
    i += 1

sw.start()
time.sleep(5)
print(f"Elapsed time: {sw.elapsed_time()}")
sw.reset()
print(f"Elapsed time: {sw.elapsed_time()}")