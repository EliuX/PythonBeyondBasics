
class Container:
    next_serial = 2234

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def create_empty_cargo():
        return Container("EMPTY", None)

    def create_name(cls, id):
        return "C" + id

    def __init__(self, id, content):
        global prefix
        self.id = self.create_name(id)
        self.serial = Container._get_next_serial()
        self.content = content

    def get_id(self):
        return self.id

    def get_serial(self):
        return self.serial

    def get_content(self):
        return self.content

class RefrigeratedContainer(Container):

    MAX_CELSIUS = 4.0   #class attribute

    @staticmethod
    def create_empty_cargo():
        return RefrigeratedContainer('EMPTY', ['ice'])

    @classmethod
    def create_name(cls, id):
        return "R" + id
    
    def __init__(self, id, content, temperature):
        super(RefrigeratedContainer, self).__init__(id, content)
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value > RefrigeratedContainer.MAX_CELSIUS:
            raise ValueError('Too high value')
        self._temperature = value

if __name__ == "__main__":
    refrigeratedContainer = RefrigeratedContainer ("XBASEEF", ['fish', 'chicken'], 3)
    refrigeratedContainer.temperature = 4
    print(refrigeratedContainer.temperature)
