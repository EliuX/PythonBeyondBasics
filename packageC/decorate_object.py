class Count():
  def __init__(self, maxcount=-1): 
    self.counter = {}
    self.maxcount = maxcount

  def __call__(self, f): 
    def create_counter(num):
      if num not in self.counter:
        self.counter[num] = 0
      if self.maxcount < 0 or self.counter[num] < self.maxcount:
        self.counter[num]+=1
        print("Its the {} time you".format(self.counter[num]))
      return f(num)
    return create_counter

  def state(self):
    return "{}/{}".format(self.counter, self.maxcount)

count_up_to_3 = Count(3)   

@count_up_to_3
def add_value(num): 
  return "add " + str(num)

@Count()
def remove_value(num): 
  return "remove " + str(num) 

def test_object_decorator():
  print(add_value(1))
  print(add_value(2)) 
  print(add_value(2)) 
  print(add_value(2))  
  print(add_value(2))  
  print(add_value(2)) 
  print(remove_value(2)) 
  print("Adder counter state: " + count_up_to_3.state())
