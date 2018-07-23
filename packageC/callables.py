import socket

class Resolver:
  def __init__(self):
    self.cache = {}

  def __call__(self, hostname):
    if hostname not in self.cache: 
      self.cache[hostname] = socket.gethostbyname(hostname)
    return self.cache[hostname]


def test_callable():
  resolve = Resolver()
  ip = resolve.__call__('google.com')
  print(ip)
  print(type(resolve))
  print(type(Resolver))
  print(type(1))

def create_sequence(immutable=True):
  return tuple if immutable else list

def test_immutable():
 immutable_seq_type = create_sequence()
 iseq = immutable_seq_type('Hello types')
 print(iseq)
 print(type(iseq))
 print(type(iseq)('Just another tuple'))

