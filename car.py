from .serviceable import Serviceable
from .Engine.engine import Engine
from .Battery.battery import Battery
from .Tyres.tyre import Tyre

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tyre: Tyre):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre

    def needs_service(self) -> bool:
        return (self.engine.needs_service() 
                or self.battery.needs_service() 
                or self.tyre.needs_service())