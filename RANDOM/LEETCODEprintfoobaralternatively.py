from threading import Event
class FooBar:
    def __init__(self, n):
        self.n = n
        self.e1=Event()
        self.e2=Event()
        self.e1.set()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.e1.wait()
            printFoo()
            self.e1.clear()
            self.e2.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.e2.wait()
            printBar()
            self.e2.clear()
            self.e1.set()
