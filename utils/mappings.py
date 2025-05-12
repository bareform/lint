from ..rules import (
  EndsWithSingleNewline,
  EachLineLessThanXChars,
  NoTrailingWhitespaces
)

strip_end_of_file_newlines = "strip_end_of_file_newlines"
max_line_len = "max_line_len"
no_trailing_whitespaces = "no_trailing_whitespaces"

valid_keys = (
  strip_end_of_file_newlines,
  max_line_len,
  no_trailing_whitespaces
)

key_to_rule_mapping = {
  strip_end_of_file_newlines: EndsWithSingleNewline,
  max_line_len: EachLineLessThanXChars,
  no_trailing_whitespaces: NoTrailingWhitespaces
}

key_to_required_type = {
  strip_end_of_file_newlines: bool,
  max_line_len: int,
  no_trailing_whitespaces: bool
}
