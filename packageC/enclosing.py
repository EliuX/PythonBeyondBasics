

def create_salute(salute_phrase): 
  def say_hello(who):
    return "{} {}".format(salute_phrase, who)
  return say_hello


def test_simple_closure():
  salute = create_salute("Hello");
  print(salute("World"))
  print(salute("EliuX"))