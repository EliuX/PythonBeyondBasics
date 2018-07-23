
_Container__prefix = "cnt"

class Container:
    next_serial = 2234

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty_cargo(cls):
        return cls("EMPTY", None)

    def __init__(self, id, content):
        global prefix
        self.id = __prefix + id
        self.serial = Container._get_next_serial()
        self.content = content

    def get_id(self):
        return self.id

    def get_serial(self):
        return self.serial


if __name__ == "__main__":
    cntr = Container("CHCARGO", ['pees','onions','garlic'])

    print(cntr.id)
    print(cntr.get_serial())
    print(cntr._get_next_serial())

    emptyContainer = Container.create_empty_cargo()
    print(emptyContainer.get_id())