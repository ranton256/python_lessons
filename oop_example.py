

class Vehicle:
    """This class represents any type of vehicle with max speed, seating and weight."""
    def __init__(self, max_speed, weight, seating_capacity):
        # set member variables (attributes or fields)
        self.max_speed = max_speed
        self.weight = weight
        self.seating_capacity = seating_capacity
        self.passengers = []
        self.speed = 0.0

    def get_weight(self):
        return self.weight

    def get_max_speed(self):
        return self.max_speed

    def get_speed(self):
        return self.speed

    def accelerate(self, amount):
        self.speed = self.speed + amount
        if self.speed < 0.0:
            self.speed = 0.0
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def speed_up(self):
        self.accelerate(10)

    def slow_down(self):
        self.accelerate(-10)

    def get_seating_capacity(self):
        return self.seating_capacity

    def add_passenger(self, passenger_name):
        if len(self.passengers) >= self.get_seating_capacity():
            return False  # or we could throw an exception here.
        else:
            self.passengers.append(passenger_name)

    def get_passengers(self):
        return self.passengers.copy()

    def __str__(self):
        return "Vehicle(max_speed: {}, weight: {}, seats: {}, speed: {}, passengers: {}".format(
            self.max_speed, self.weight, self.seating_capacity, self.speed,
            ",".join(self.passengers)  # comma separated list of passengers
        )

class Bicycle(Vehicle):

    def __init__(self):
        # This requires Python 3 or newer.
        super().__init__(30, 40, 1)

    def __str__(self):
        bs = super().__str__()
        return "Bicycle: " + bs



def main():
    my_vehicle = Vehicle(40.0, 2800, 4)
    print ("My vehicle is {}". format(my_vehicle))
    my_vehicle.add_passenger("Richard")
    print("The passengers are {}".format(my_vehicle.get_passengers()))
    print("My vehicle is {}".format(my_vehicle))
    for i in range(5):
        my_vehicle.speed_up()
        print("My vehicle is {}".format(my_vehicle))
    for i in range(5):
        my_vehicle.slow_down()
        print("My vehicle is {}".format(my_vehicle))

    my_bike = Bicycle()
    my_bike.add_passenger("Richard")
    print("My bike is {}".format(my_bike))

if __name__ == "__main__":
    # execute only if run as a script
    main()

