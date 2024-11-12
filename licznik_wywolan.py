import functools

def count_calls(func):
        def wrapper(*args, **kwargs):
            if not hasattr(wrapper, "call_count"):
                wrapper.call_count = 0
            wrapper.call_count += 1
            print(f"Function {func.__name__} has been called {wrapper.call_count} times.")
            return func(*args, **kwargs)
        return wrapper

class FuntionCallTracker:
    def __init__(self, func):
        self.func = count_calls(func)
        self.total_calls = 0

    def reset(self):
        self.total_calls = 0
        if not hasattr(self.func, "call_count"):
             self.func.call_count = 0

    def __call__(self, *args, **kwds):
        self.total_calls += 1
        return self.func(*args, **kwargs)
    
@FuntionCallTracker    #dekorator
def my_function():
     print("My function is running!")

     