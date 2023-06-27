from abc import ABC, abstractmethod
from datetime import date

class Battery(ABC):
    @abstractmethod
    def needs_service(self,) -> bool:
        pass
    
    
class SpindlerBattery:
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date: date = last_service_date
        self.current_date: date = current_date 
        
    def needs_service(self) -> bool:
        service_threshold_date: date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < date.today():
            return True
        else:
            return False
        

class NubbinBattery:
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < date.today():
            return True
        else:
            return False