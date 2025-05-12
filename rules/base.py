class Rule:
  def _read_file(self, path: str) -> str:
    with open(path, "r") as file:
      content = file.read()
    return content
  
  def _write_file(self, path: str, content: str) -> None:
    with open(path, "w") as file:
      file.write(content)
  
  def _fix(self, path: str) -> str:
    raise NotImplementedError

  def fix(self, path: str) -> None:
    raise NotImplementedError

  def check(self, path: str) -> bool:
    raise NotImplementedError

  def get_error_message(self, *args: tuple, **kwargs: dict[str, str]) -> str:
    raise NotImplementedError
