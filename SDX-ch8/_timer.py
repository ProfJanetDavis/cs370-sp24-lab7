from mock_object import Fake
from time import time

class Timer():
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Elapsed time: {self.elapsed()} seconds")

    def elapsed(self):
        return time() - self.start
        
if __name__ == '__main__':
    with Timer() as timer:
        print(timer.elapsed())
        for i in range(1000000):
            pass
        print(timer.elapsed())
        for i in range(10000000):
            pass
        print(timer.elapsed())
        for i in range(100000000):
            pass