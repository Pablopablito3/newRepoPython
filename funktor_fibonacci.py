class FibonacciGenerator():
    def __init__(self, a = 0, b = 1):
        self.a = a
        self.b = b

    def __call__(self):
        next_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return next_value
    
fib_gen = FibonacciGenerator()

for _ in range(10):
    print(fib_gen())



