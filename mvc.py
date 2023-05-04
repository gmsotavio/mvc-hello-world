class Model:
    def __init__(self):
        self.value = 0
    
    def increment(self):
        self.value += 1
    
    def decrement(self):
        self.value -= 1
    
    def getValue(self):
        return self.value


class View:
    def display(self, value):
        print(f"The current value is {value}")


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def increment(self):
        self.model.increment()
        self.view.display(self.model.getValue())
    
    def decrement(self):
        self.model.decrement()
        self.view.display(self.model.getValue())


# Example usage
model = Model()
view = View()
controller = Controller(model, view)

# Increment the value using the controller
controller.increment()  # Output: The current value is 1

# Decrement the value using the controller
controller.decrement()  # Output: The current value is 0

