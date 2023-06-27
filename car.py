from serviceable import Serviceable
from Engine import engine
from Battery import battery

class Car(Serviceable):
    def __init__(self, engine: engine, battery: battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()