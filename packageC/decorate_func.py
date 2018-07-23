def count_up_to(maxcounter):
  def count(f):
    counter = {}
    def track_and_print(num):
      nonlocal counter
      if num not in counter:
        counter[num]=0
      if(maxcounter < 0 or counter[num] < maxcounter):  
        counter[num]+=1
        print("Its the {} time you".format(counter[num]))
      return f(num)
    return track_and_print
  return count

count_all = count_up_to(-1)  

@count_up_to(3)
def add_value(num): 
 return "add " + str(num)

@count_all
def remove_value(num): 
  return "remove " + str(num) 

def test_func_decorator():
  print(add_value(1))
  print(add_value(2)) 
  print(add_value(2)) 
  print(add_value(2))  
  print(add_value(2))  
  print(add_value(2)) 
  print(remove_value(2)) 