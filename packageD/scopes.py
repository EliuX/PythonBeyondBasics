
_my_private_var = "This Str is meant for internal use only in this module"

_Container__prefix = "cnt"

class Container:

    next_serial = 2234

    def __init__(self, id):
        global prefix
        self.id = __prefix + id
        self.serial = Container.next_serial
        Container.next_serial += 1

    def _get_next_serial(self):
        return self.next_serial

    def get_id(self):
        return self.id

    def get_serial(self):
        return self.serial


if __name__ == "__main__":
   cntr = Container("CHCARGO")

   print(cntr.id)
   print(cntr.get_serial())
   print(cntr._get_next_serial())