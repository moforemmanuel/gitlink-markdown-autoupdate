

class User_Model:
  
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

  def get_name(self) -> str:
    if (not isinstance(self.name, str)):
      raise TypeError
    return f"Hi, I'm ${self.name}"
  
  def get_age(self) -> str:
    return f"Hi, I'm ${self.age} years old"