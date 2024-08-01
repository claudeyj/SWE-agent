#!/usr/bin/env python3

"""This helper command is used to print java linting output (from javac-parser
library)in a readable format

Usage:
    python _java_linting.py <java_file_content>
"""

import sys
from pathlib import Path
import javac_parser


def format_check_syntax_output(
    input_string:str,
    show_line_numbers: bool = True
    ) -> str:
    """Extract the output of the check_syntax function to a readable format

    Args:
        input_string: The content of the java file
        show_line_numbers: Whether to show line numbers in the output
    """
    java = javac_parser.Java()
    errors = java.check_syntax(input_string)
    lines = []

    for error in errors:
        err_kind, err_code, err_msg, line_num, _, _, _ = error

        if not show_line_numbers:
            lines.append(f"[{err_kind}]: {err_msg}")
        else:
            lines.append(f"[{err_kind}] at line {line_num}: {err_msg}")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(format_check_syntax_output(Path(sys.argv[1]).read_text()))
    else:
        raise ValueError("Usage: python _java_linting.py <java_file>")