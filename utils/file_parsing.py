import os
import re

def file_exists(path: str) -> bool:
  if os.path.exists(path) and os.path.isfile(path):
    return True
  return False

def parse_run_command_file(path: str) -> dict[str, str]:
  if file_exists(path):
    with open(path, "r") as file:
      content = file.read()
    content = content.strip()
    content = re.sub(r"[^\S\n]+", "", content)
    content = content.split("\n")
    run_commands = {rule: value for rule, value in (pair.split("=") for pair in content)}
    return run_commands
  return {}

def parse_ignore_file(path: str) -> list[str]:
  if file_exists(path):
    with open(path, "r") as file:
      content = file.read()
    content = content.strip().split("\n")
    return content
  return []
