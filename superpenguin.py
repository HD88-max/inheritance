# Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.
class bird:
    def __init__(self):
        print("The bird is ready to fly.")
    def fly(self):
        print("Bird")
    def swim(self):
        print("Swims faster")
    
class penguin(bird):
    def __init__(self):
        print("Penguin is ready")
    def fly(self):
        print("Penguin")
    def run(self):
        print("Runs faster")
pengu = penguin()
pengu.fly()
pengu.swim()
pengu.run()