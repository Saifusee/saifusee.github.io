#Another example for airline booking example
class Flight:

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    

indian_airways = Flight(capacity=3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if indian_airways.add_passenger(people):
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")

