def is_int(value: str) -> bool:
  return value.isdigit()

def is_bool(value: str) -> bool:
  return value in ["True", "False"]
