class Car:
    def start(self):
        pass

    def stop(self):
        pass


class BMW(Car):
    def start(self):
        return "BMW is starting."

    def stop(self):
        return "BMW is stopping."


class Ferrari(Car):
    def start(self):
        return "Ferrari is starting."

    def stop(self):
        return "Ferrari is stopping."



bmw = BMW()
ferrari = Ferrari()

print(bmw.start())
print(bmw.stop())
print()
print(ferrari.start()) 
print(ferrari.stop())
