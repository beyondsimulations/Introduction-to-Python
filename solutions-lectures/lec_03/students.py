class Students: # Superclass
    def __init__(self, name):
        self.name = name

class SmartStudents(Students): # Subclass
    def when_asked(self):
        return f"{self.name} knows the answer!"

class LazyStudents(Students): # Subclass
    def when_asked(self):
        return f"{self.name} has to ask ChatGPT!"

adam = LazyStudents("Adam")
eve = SmartStudents("Eve")

print(adam.when_asked())
print(eve.when_asked())
