class Function:
    def apply(self, value):
        pass

def fill(array, function_instance):
    for i in range(len(array)):
        array[i] = function_instance.apply(i)

class SquareFunction(Function):
    def apply(self, value):
        return value * value