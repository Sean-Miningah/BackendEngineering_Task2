from datetime import date
from .Engine.engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from .Battery.battery import NubbinBattery, SpindlerBattery
from .car import Car

class CarFactory:
    def __init__(self):
        pass 
    
    def create_calliope(
            current_date: date, 
            last_service_date: date, 
            current_mileage: int, 
            last_service_mileage: int
        ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine, battery)
        
    def create_thovex(
            last_service_mileage: int,
            current_mileage: int,
            current_date: date,
            last_service_date: date
        ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine, battery)
    
    def create_glissade(
            last_service_mileage: int,
            current_mileage: int,
            current_date: date,
            last_service_date: date
        ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine, battery)
    
    def create_palindrome(
            warning_light_on: bool,
            current_date: date,
            last_service_date: date
        ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine, battery)
    
    def create_rorschach(
            last_service_mileage: int,
            current_mileage: int,
            current_date: date,
            last_service_date: date
        ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine, battery)