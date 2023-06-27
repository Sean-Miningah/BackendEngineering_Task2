from abc import ABC, abstractmethod
from typing import List

class Tyre(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
    

class CarriganTyre(Tyre):
    def __init__(self, tyre_wear: List[float]):
        self.tyre_wear = tyre_wear
        
    def needs_service(self) -> bool:
        for tyre in self.tyre_wear:
            if tyre >= 0.9:
                return True
        return False
            
class OctoprimeTyre(Tyre):
    def __init__(self, tyre_wear: List[float]) -> None:
        self.tyre_wear: List[float] = tyre_wear 
        
    def needs_service(self) -> bool:
        return sum(self.tyre_wear) >= 3