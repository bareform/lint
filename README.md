## Lint

Lint is a tool for identifying and reporting on patterns in Python code.

- Lint uses static line-by-line analysis.
- Lint is meant to be completely pluggable in any Python codebase.
- Lint is meant to be customizable.

### Table of Contents

1. [Installation and Usage](#installation-and-usage)
1. [Configuration](#configuration)
1. [Rules](#rules)

### Installation and Usage

Prerequisites: [Python3](https://www.python.org/downloads/release/python-390/) or higher (^`3.9.0`).

You can install and configure Lint using the command:

```console
git submodule add https://github.com/bareform/lint path/to/folder
git submodule update --remote --merge
git commit -m "added lint"
```

After that, you can run Lint on any file or directory like this:

```console
python3 -m lint yourfile.py
```

### Configuration

You can configure rules in your `.lintrc` file as in this example:

```
strip_end_of_file_newlines = True
max_line_len = 120
no_trailing_whitespaces = True
```

The names `"strip_end_of_file_newlines"`, `"max_line_len"`, and `"no_trailing_whitespaces"` are the names of rules in Lint.

You can selectively ignore a file or directory by using a `.lintignore` as in this example:

```
path/to/folder/yourfile.py
```

### Rules

#### `strip_end_of_file_newlines`

**Description**

This rule enforces that each file ends with exactly one newline character. 

**Options**

This rule accepts two different values:

- `True`: When set to `True`, enable this rule.
- `False`: When set to `False`, disable this rule.

Fixable by Lint: `Yes`

---

#### `max_line_len`

**Description**

This rule enforces a maximum line length for readability.

**Options**

This rule accepts a simgle numeric integer value:

- A number representing the maximum number of characters allowed per line.

Fixable by Lint: `No`

---

#### `no_trailing_whitespaces`

**Description**

This rule enforces that each line does not end with whitespace.

**Options**

This rule accepts two different values:

- `True`: When set to `True`, enable this rule.
- `False`: When set to `False`, disable this rule.

Fixable by Lint: `Yes`

---

You can run Lint with the `--fix` flag to apply any changes that need to be made:

```console
python3 -m lint --fix yourfile.py
```
