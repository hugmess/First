class Car():
    def __init__(self, color, manufacture, model, number, headlights, motor):
        self.color = color
        self.manufacture = manufacture
        self.model = model
        self.CarNumber = number
        self.headlights = headlights
        self.motor = motor

    def ShowInfo(self):
        print(self.headlights)
        print(self.motor)
        print(self.model)
        print(self.manufacture)
        print("Color" + self.color)
        print("CarNumber" + self.CarNumber)

    def lg(self):
        if(self.headlights == "On"):
            self.headlights == "Off"
        else:
            self.headlights == "On"

    def mt(self):
        if(self.motor == "On"):
            self.motor == "Off"
        else:
            self.motor == "On"

HarryCar = Car("Yellow","BMW", "M5", "AE4827AO", "Off", "On")
JackCar = Car("White","BMW", "525i", "KA3482HH","On", "On")

HarryCar.ShowInfo()
JackCar.ShowInfo()
