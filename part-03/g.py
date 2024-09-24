class Student: # Superclass
    def __init__(self, name):
        self.name = name
    def when_asked(self):
        pass

class SmartStudent(Student): # Subclass
    def when_asked(self):
        return f"{self.name} knows the answer!"
        
class LazyStudent(Student): # Subclass
    def when_asked(self):
        return f"{self.name} has to ask ChatGPT!"
    
lisa = SmartStudent("Lisa")
ted = LazyStudent("Ted")

print(lisa.when_asked())
print(ted.when_asked())