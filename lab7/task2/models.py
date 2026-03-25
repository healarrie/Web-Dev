class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"Двигатель {self.brand} запущен."

    def drive(self):
        return f"{self.model} в движении."

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def drive(self):
        return f"Машина {self.model} едет по дороге на {self.fuel_type}."

class Airplane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude

    def fly(self):
        return f"{self.model} взлетает на высоту {self.max_altitude}м."

    def drive(self):
        return f"Самолет {self.model} выруливает на взлетную полосу."