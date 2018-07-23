

def test_lambdas():
 mult3 = list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
 print(mult3)

def test_list_comprehension():
  mult3 = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 3 == 0]
  print(mult3)