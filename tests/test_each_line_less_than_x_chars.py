from rules import EachLineLessThanXChars

import os

def test_simple_case():
  rule = EachLineLessThanXChars(x=120)
  test_files_simple_file = os.path.join("tests", "test_files", "each_line_less_than_x_chars", "simple.py")
  test_case_status = []
  if not rule.check(test_files_simple_file):
    print("Successfully catch a stylistic error (a line of code is too long)")
    test_case_status.append(True)
  else:
    print("Failed to successfully catch a stylistic error (a line of code is too long")
    test_case_status.append(False)

  if rule.violating_lines == [11]:
    print("Successfully identify the line with a stylistic error")
    test_case_status.append(True)
  else:
    print("Failed to identify the correct line with a stylistic error")
    test_case_status.append(False)
  return all(test_case_status)

def test_complex_case():
  rule = EachLineLessThanXChars(x=120)
  test_files_simple_file = os.path.join("tests", "test_files", "each_line_less_than_x_chars", "complex.py")
  test_case_status = []
  if not rule.check(test_files_simple_file):
    print("Successfully catch a stylistic error (a line of code is too long)")
    test_case_status.append(True)
  else:
    print("Failed to successfully catch a stylistic error (a line of code is too long")
    test_case_status.append(False)

  if rule.violating_lines == [2, 6, 10, 16, 17, 18, 24, 26, 28]:
    print("Successfully identify the line with a stylistic error")
    test_case_status.append(True)
  else:
    print("Failed to identify the correct line with a stylistic error")
    test_case_status.append(False)
  return all(test_case_status)

def main():
  test_cases = {
    "SIMPLE": test_simple_case,
    "COMPLEX": test_complex_case
  }
  results = []
  print("Testing EachLineLessThanXChars Rule implementation...")
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
    print("Passed all test cases for EachLineLessThanXChars!")
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
