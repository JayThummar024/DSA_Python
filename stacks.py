
###########################################  Stack using lists ###########################################

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(i) for i in self.list]
        return "\n".join(values)

    def push(self,element):
        self.list.append(element)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False




