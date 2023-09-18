from servicable import Serviceable

class Car(Serviceable):
        def __init__(self, engine, battery):
             self.engine = engine
             self.battery = battery
        
        def needs_service(self):
               service_result = self.engine.needs_service() or self.battery.needs_service()
               return service_result
        
