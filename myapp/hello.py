import fire

def hello(name="World"):
  return "Helloo %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)