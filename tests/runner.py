from .test_ends_with_single_newline import (
  main as test_ends_with_single_newline_main
)
from .test_each_line_less_than_x_chars import (
  main as test_each_line_less_than_x_chars_main
)
from .test_no_trailing_whitespaces import (
  main as test_no_trailing_whitespaces_main
)

def main():
  runner = {
    "test_ends_with_single_newline": test_ends_with_single_newline_main,
    "test_each_line_less_than_x_chars": test_each_line_less_than_x_chars_main,
    "test_no_trailing_whitespaces": test_no_trailing_whitespaces_main
  }
  results = []
  for test_case_file_main_fn in runner.values():
    test_case_file_main_result = test_case_file_main_fn()
    results.append(test_case_file_main_result)
    print()
  if all(results):
    print("Passed all test cases!")
  else:
    print("FAILED")
    print("Failed the following test cases:")
    for test_case_idx, test_case_file in enumerate(runner.keys()):
      if not results[test_case_idx]:
        print(f"  - {test_case_file}")

if __name__ == "__main__":
  main()
