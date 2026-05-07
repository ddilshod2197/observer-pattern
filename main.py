from abc import ABC, abstractmethod

# Abstract Product
class Transport(ABC):
    @abstractmethod
    def transport(self):
        pass

# Concrete Products
class Car(Transport):
    def transport(self):
        return "Car is transporting"

class Truck(Transport):
    def transport(self):
        return "Truck is transporting"

class Ship(Transport):
    def transport(self):
        return "Ship is transporting"

# Factory
class TransportFactory:
    @staticmethod
    def create_transport(type):
        if type == "car":
            return Car()
        elif type == "truck":
            return Truck()
        elif type == "ship":
            return Ship()
        else:
            raise ValueError("Invalid transport type")

# Client code
def main():
    factory = TransportFactory()
    car = factory.create_transport("car")
    truck = factory.create_transport("truck")
    ship = factory.create_transport("ship")

    print(car.transport())
    print(truck.transport())
    print(ship.transport())

if __name__ == "__main__":
    main()
```

Kodda Factory patterni quyidagicha ishlatiladi:

1. `Transport` abstract classi (Abstract Product) transport vositalarini ifodalaydi.
2. `Car`, `Truck` va `Ship` klasslari (Concrete Products) transport vositalarining turli xil turlarini ifodalaydi.
3. `TransportFactory` klassi (Factory) transport vositalarini yaratish uchun muhim metodlarni ifodalaydi.
4. `main` funksiyasi (Client code) transport vositalarini yaratish uchun `TransportFactory` klassidan foydalanadi.
