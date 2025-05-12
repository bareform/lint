from rules import NoTrailingWhitespaces

import os

def test_simple_case():
  rule = NoTrailingWhitespaces()
  solutions_simple_file = os.path.join("tests", "solutions", "no_trailing_whitespaces", "simple.py")
  test_files_simple_file = os.path.join("tests", "test_files", "no_trailing_whitespaces", "simple.py")
  test_case_status = []
  if not rule.check(test_files_simple_file):
    print("Successfully catch a stylistic error (a line of code has trailing whitespace)")
    test_case_status.append(True)
  else:
    print("Failed to successfully catch a stylistic error (a line of code has trailing whitespace")
    test_case_status.append(False)

  if rule.violating_lines == [3]:
    print("Successfully identify the line with a stylistic error")
    test_case_status.append(True)
  else:
    print("Failed to identify the correct line with a stylistic error")
    test_case_status.append(False)

  if rule._fix(test_files_simple_file) == rule._read_file(solutions_simple_file):
    print("Suggested fix matches reference")
    test_case_status.append(True)
  else:
    print("Suggested fix does not match reference")
    test_case_status.append(False)
  return all(test_case_status)

def test_complex_case():
  rule = NoTrailingWhitespaces()
  solutions_complex_file = os.path.join("tests", "solutions", "no_trailing_whitespaces", "complex.py")
  test_files_complex_file = os.path.join("tests", "test_files", "no_trailing_whitespaces", "complex.py")
  test_case_status = []
  if rule.check(solutions_complex_file):
    print("A file with no stylistic error passed")
    test_case_status.append(True)
  else:
    print("A file with no stylistic error did not passed")
    test_case_status.append(False)

  if not rule.check(test_files_complex_file):
    print("Successfully catch a stylistic error (a line of code has trailing whitespace)")
    test_case_status.append(True)
  else:
    print("Failed to successfully catch a stylistic error (a line of code has trailing whitespace")
    test_case_status.append(False)

  if rule.violating_lines == [3, 7, 11, 16, 21, 24, 27]:
    print("Successfully identify the line with a stylistic error")
    test_case_status.append(True)
  else:
    print("Failed to identify the correct line with a stylistic error")
    test_case_status.append(False)
  if rule._fix(test_files_complex_file) == rule._read_file(solutions_complex_file):
    print("Suggested fix matches reference")
    test_case_status.append(True)
  else:
    print("Suggested fix does not match reference")
    test_case_status.append(False)
  return all(test_case_status)

def main():
  test_cases = {
    "SIMPLE": test_simple_case,
    "COMPLEX": test_complex_case
  }
  results = []
  print("Testing NoTrailingWhitespaces Rule implementation...")
  print("DETAILED REPORT")
  print("---------------")
  for test_case_name, test_case_func in test_cases.items():
    print(f"Problem: {test_case_name}")
    print("Feedback")
    test_case_status = test_case_func()
    if test_case_status:
      print("PASSED")
    else:
      print("FAILED")
    print("---------------")
    results.append(test_case_status)
  if all(results):
    print("Passed all test cases for NoTrailingWhitespaces!")
  else:
    print("FAILED")
    print("Failed the following test cases:")
    for test_case_idx, test_case_name in enumerate(test_cases.keys()):
      if not results[test_case_idx]:
        print(f"  - {test_case_name}")
    return False
  return True

if __name__ == "__main__":
  main()
