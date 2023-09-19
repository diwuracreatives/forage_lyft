from main import Engine

class SternmanEngine(Engine):
    def __init__(self, is_warning_light_on):
        self.is_warning_light_on = is_warning_light_on

    def needs_service(self):
       if self.is_warning_light_on == True:
           return True
       else:
           return False