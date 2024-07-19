import re

# Sample file name
file = "example.file.name.txt"

def rename_extension(file, new_extension=".xlsx"):
    # Regex pattern to find the last dot
    # \.: The backslash (\) escapes the dot (.), making it a literal character in the pattern. Without the backslash, a dot in a regular expression matches any character except a newline. With the backslash, it matches an actual dot
    # ( and ): These are capturing parentheses, which capture the part of the string matched by the regex inside them for later use. In this case, it captures everything after the last dot.
    # [^.]: The square brackets define a character class, and the caret (^) at the beginning negates the character class, meaning it matches any character except those specified. Here, it matches any character except a dot.
    # *: This quantifier matches zero or more occurrences of the preceding element ([^.] in this case). Combined with [^.], it matches any sequence of characters that does not contain a dot.
    # $: This anchor matches the end of the string.
    pattern = r"\.([^.]*)$"

    # Finding the match
    match = re.search(pattern, file)
    if match:
        last_dot_position = match.start()
        # Slice the string up to the dot and append the new extension
        new_file_name = file[:last_dot_position] + new_extension
    else:
        # No dot found, keep the original file name
        new_file_name = file

    return new_file_name
