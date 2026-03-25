from models import Car, Airplane

def main():
    my_car = Car("Toyota", "Camry", 2024, "Бензин")
    my_plane = Airplane("Boeing", "747", 2022, 10000)

    vehicles = [my_car, my_plane]

    print("--- Демонстрация работы объектов ---")

    for v in vehicles:
        print(f"Транспорт: {v}") 
        
        print(f"Действие: {v.drive()}")
        
        print(f"Статус: {v.start_engine()}")
        print("-" * 30)

    print(my_plane.fly())

if __name__ == "__main__":
    main()