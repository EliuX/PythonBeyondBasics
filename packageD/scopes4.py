
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

    @staticmethod
    def create_empty_cargo():
        return RefrigeratedContainer('EMPTY', ['ice'])

    @classmethod
    def create_name(cls, id):
        return "R" + id

if __name__ == "__main__":
    emptyContainer = Container.create_empty_cargo()
    print(emptyContainer.id)
    print(emptyContainer.get_content())

    emptyRefrigeratedContainer = RefrigeratedContainer.create_empty_cargo()
    print(emptyRefrigeratedContainer.id)      # Encapsulation is a not a recommended practice
    print(emptyRefrigeratedContainer.get_content())
