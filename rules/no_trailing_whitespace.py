from .base import Rule

class NoTrailingWhitespaces(Rule):
  def __init__(self) -> None:
    self.violating_lines = []

  def __repr__(self) -> str:
    return (
      "NoTrailingWhitespaces(" +
      f"violating_lines=[{', '.join([
        str(line) for line in self.violating_lines]) if len(self.violating_lines) > 0 else ''}]" +
      ")"
    )

  def _fix(self, path: str) -> str:
    content = self._read_file(path).split("\n")
    content = "\n".join([line.rstrip() for line in content])
    return content

  def fix(self, path: str) -> None:
    content = self._fix(path)
    self._write_file(path, content)

  def check(self, path: str) -> bool:
    content = self._read_file(path).split("\n")
    for line_number, line in enumerate(content):
      if line != line.rstrip():
        self.violating_lines.append(line_number + 1)
    return len(self.violating_lines) == 0
  
  def get_error_message(self, *args: tuple, **kwargs: dict[str, str]) -> str:
    if "file" not in kwargs:
      raise ValueError("missing required keyword argument: 'file'")
    if "line_number" not in kwargs:
      raise ValueError("missing required keyword argument: 'line_number'")
    return f"Caught a stylistic error in {kwargs['file']} on line {kwargs['line_number']} (trailing whitespaces)"
