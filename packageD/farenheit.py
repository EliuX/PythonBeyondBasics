
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
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def create_empty_cargo():
        return RefrigeratedContainer('EMPTY', ['ice'])

    @classmethod
    def create_name(cls, id):
        return "R" + id
    
    def __init__(self, id, content, celsius):
        super(RefrigeratedContainer, self).__init__(id, content)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedContainer.MAX_CELSIUS:
            raise ValueError('{} is too hot!'.format(value))
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        return RefrigeratedContainer._f_to_c(value)


if __name__ == "__main__":
    refrigeratedContainer = RefrigeratedContainer ("XBASEEF", ['fish', 'chicken'], -20)
    print(refrigeratedContainer.celsius)
    print(refrigeratedContainer.fahrenheit)

