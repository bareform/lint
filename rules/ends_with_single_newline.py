from .base import Rule

class EndsWithSingleNewline(Rule):
  def __repr__(self) -> str:
    return "EndsWithSingleNewline()"

  def _fix(self, path: str) -> str:
    content = self._read_file(path).strip("\n") + "\n"
    return content

  def fix(self, path: str) -> None:
    content = self._fix(path)
    self._write_file(path, content)

  def check(self, path: str) -> bool:
    content = self._read_file(path)
    return content.endswith("\n") and not content.endswith("\n\n")

  def get_error_message(self, *args: tuple, **kwargs: dict[str, str]) -> str:
    if "file" not in kwargs:
      raise ValueError("missing required keyword argument: 'file'")
    return f"Caught a stylistic error in {kwargs['file']} (more than one newline character at end of file)"
