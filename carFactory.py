from datetime import date
from typing import List
from .Engine.engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from .Battery.battery import NubbinBattery, SpindlerBattery
from .car import Car
from .Tyres.tyre import CarriganTyre, OctoprimeTyre

class CarFactory:
    def __init__(self):
        pass 
    
    def create_calliope(
            current_date: date, 
            last_service_date: date, 
            current_mileage: int, 
            last_service_mileage: int,
            tyre_wear: List[float]
        ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        tyre = CarriganTyre(tyre_wear)
        return Car(engine, battery, tyre)
        
    def create_thovex(
            last_service_mileage: int,
            current_mileage: int,
            current_date: date,
            last_service_date: date,
            tyre_wear: List[float]
        ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        tyre = CarriganTyre(tyre_wear)
        return Car(engine, battery, tyre)
    
    def create_glissade(
            last_service_mileage: int,
            current_mileage: int,
            current_date: date,
            last_service_date: date,
            tyre_wear: List[float]
        ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        tyre = CarriganTyre(tyre_wear)
        return Car(engine, battery, tyre)
    
    def create_palindrome(
            warning_light_on: bool,
            current_date: date,
            last_service_date: date,   
            tyre_wear: List[float]
        ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        tyre = CarriganTyre(tyre_wear)
        return Car(engine, battery, tyre)
    
    def create_rorschach(
            last_service_mileage: int,
            current_mileage: int,
            current_date: date,
            last_service_date: date,
            tyre_wear: List[float]
        ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        tyre = CarriganTyre(tyre_wear)
        return Car(engine, battery, tyre)