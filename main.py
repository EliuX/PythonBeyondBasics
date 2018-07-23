
''' Packaging apps '''

import sys
# import packageA
# from model.Developer import Developer
# import model.Person

#developer = Developer('Linus Torvalds', 'C', 'C++')
#print(developer)

#print(model.__path__)

#print(model.Person.Person('Linus Torvalds'))

''' Functions '''
# from packageC.geometry import test_triangle

#test_triangle()

''' Callables '''
# from packageC.callables import test_callable, test_immutable
#test_callable()
#test_immutable()

''' Lambdas  '''
from packageC.lambdas import test_lambdas, test_list_comprehension
#test_lambdas()
#test_list_comprehension()

''' Closure '''
from packageC.enclosing import test_simple_closure

#test_simple_closure()

''' Decorators '''
from packageC.decorate_func import test_func_decorator

#test_func_decorator()

from packageC.decorate_object import test_object_decorator

test_object_decorator()