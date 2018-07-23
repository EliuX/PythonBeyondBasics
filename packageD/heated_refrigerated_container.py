from farenheit import RefrigeratedContainer

class HeatedRefrigeratedContainer(RefrigeratedContainer):

    MIN_CELSIUS = -20.0

    @RefrigeratedContainer.celsius.setter
    def celsius(self, value):
        if  HeatedRefrigeratedContainer.MIN_CELSIUS > value:
            raise ValueError('{} is too cold!'.format(value))
        RefrigeratedContainer.celsius.fset(self, value)

if __name__ == '__main__':
    container = HeatedRefrigeratedContainer('HOT', ['pinables', 'apples'], 1)
    container.celsius = -21
    print('New temperature is {} oC'.format(container.celsius))

