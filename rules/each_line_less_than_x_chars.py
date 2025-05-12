from .base import Rule

class EachLineLessThanXChars(Rule):
  def __init__(self, x: int=120) -> None:
    self.x = x
    self.violating_lines = []

  def __repr__(self) -> str:
    return (
      "EachLineLessThanXChars(\n" +
      f"  x={self.x},\n" +
      f"  violating_lines=[{', '.join([
        str(line) for line in self.violating_lines]) if len(self.violating_lines) > 0 else ''}]\n" +
      ")"
    )

  def check(self, path: str) -> bool:
    content = self._read_file(path).split("\n")
    for line_number, line in enumerate(content):
      if self.x < len(line):
        self.violating_lines.append(line_number + 1)
    return len(self.violating_lines) == 0

  def get_error_message(self, *args: tuple, **kwargs: dict[str, str]) -> str:
    if "file" not in kwargs:
      raise ValueError("missing required keyword argument: 'file'")
    if "line_number" not in kwargs:
      raise ValueError("missing required keyword argument: 'line_number'")
    return (
      f"Caught a stylistic error in {kwargs['file']} on line {kwargs['line_number']} " +
      f"(line is longer than {self.x} characters)"
    )
