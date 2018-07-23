from .Person import Person

class Developer(Person):
  def __init__(self, name, *langs):
    Person.__init__(self, name)
    self.langs = langs

  def get_langs(self):
    return self.langs