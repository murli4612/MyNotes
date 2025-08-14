class My_Iterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration

my_iterator = My_Iterator(1,7)

for value in my_iterator:
    print(value)