from .utils.file_parsing import (
  file_exists,
  parse_run_command_file,
  parse_ignore_file
)
from .utils.type_checking import (
  is_int,
  is_bool
)
from .utils.mappings import (
  valid_keys,
  key_to_rule_mapping,
  key_to_required_type
)

import argparse
import fnmatch
import os

def get_argparser():
  parser = argparse.ArgumentParser(prog="lint",
                      description="static code analysis tool")
  parser.add_argument("source", type=str, help="file or directory")
  parser.add_argument("--fix", action="store_true", help="apply suggested fixes")
  return parser

def main():
  args = get_argparser().parse_args()
  files_to_lint = []
  if os.path.isfile(args.source):
    files_to_lint.append(args.source)
  if os.path.isdir(args.source):
    for root, dirs, files in os.walk(args.source):
      dirs[:] = [d for d in dirs if not d.startswith('.')]
      for file in files:
        if file.endswith(".py") and \
           not file.startswith(".") and \
           not os.path.join(root, file).startswith("./lint/"):
          files_to_lint.append(os.path.join(root, file))
  if len(files_to_lint) == 0:
    return
  
  ignore_file_file = os.path.join(".", ".lintignore")
  ignore_files = parse_ignore_file(ignore_file_file) \
                  if file_exists(ignore_file_file) else None
  if ignore_files is not None:
    files_to_remove = set()
    for ignore_file in ignore_files:
      for file in files_to_lint:
        if fnmatch.fnmatch(os.path.normpath(file), ignore_file):
          files_to_remove.add(file)
    files_to_lint = set(files_to_lint)
    files_to_lint -= files_to_remove
    files_to_lint = list(files_to_lint)

  run_commands_file = os.path.join(".", ".lintrc")
  run_commands = parse_run_command_file(run_commands_file) \
                  if file_exists(run_commands_file) else None
  if run_commands is None:
    default_run_commands_file = os.path.join("lint", ".lintrc")
    run_commands = parse_run_command_file(default_run_commands_file) \
                    if file_exists(default_run_commands_file) else None
    if run_commands is None:
      raise RuntimeError("could not locate .lintrc file")
  
  rules = []
  for key, value in run_commands.items():
    if key not in valid_keys:
      raise RuntimeError('unexpected key in .lintrc file')
    if key_to_required_type[key] is bool:
      if not is_bool(value):
        raise ValueError(f"{key} expected bool")
      rules.append(key_to_rule_mapping[key]())
    elif key_to_required_type[key] is int:
      if not is_int(value):
        raise ValueError(f"{key} expected int")
      rules.append(key_to_rule_mapping[key](int(value)))

  for file in files_to_lint:
    for rule in rules:
      file_status = rule.check(file)
      if not file_status:
        if hasattr(rule, "violating_lines"):
          while len(rule.violating_lines) != 0:
            line_number = rule.violating_lines.pop(0)
            error_message = rule.get_error_message(file=file, line_number=line_number)
            if args.fix:
              try:
                rule.fix(file)
                print(f"\033[93m{error_message}\033[0m")
              except NotImplementedError:
                print(f"\033[91m{error_message}\033[0m")
                continue
            else:
              print(f"\033[91m{error_message}\033[0m")
        else:
          error_message = rule.get_error_message(file=file)
          if args.fix:
            try:
              rule.fix(file)
              print(f"\033[93m{error_message}\033[0m")
            except NotImplementedError:
              print(f"\033[91m{error_message}\033[0m")
              continue
          else:
            print(f"\033[91m{error_message}\033[0m")

if __name__ == "__main__":
  main()
