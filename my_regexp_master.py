import re

# file = "example.file.name.txt"  
def rename_extension(file, new_extension=".xlsx"):
    r""" Regex pattern to find the last dot
    \.: The backslash (\) escapes the dot (.), making it a literal character in the pattern. Without the backslash, a dot in a regular expression matches any character except a newline. With the backslash, it matches an actual dot
    ( and ): These are capturing parentheses, which capture the part of the string matched by the regex inside them for later use. In this case, it captures everything after the last dot.
    [^.]: The square brackets define a character class, and the caret (^) at the beginning negates the character class, meaning it matches any character except those specified. Here, it matches any character except a dot.
    *: This quantifier matches zero or more occurrences of the preceding element ([^.] in this case). Combined with [^.], it matches any sequence of characters that does not contain a dot.
    $: This anchor matches the end of the string.
    """
    pattern = r"\.([^.]*)$"
    # Match Object: The match object contains information about the search and the result. It includes methods to access the matched portion of the string and its position within the original string.
    match = re.search(pattern, file)
    if match:
        # match.start() Method: The .start() method of a match object returns the starting index of the match in the original string. This means it gives you the position where the matched segment begins. If the pattern includes capturing groups (specified by parentheses in the regular expression), .start(group) can be used to get the start position of a specific group. Without any arguments, .start() defaults to returning the start position of the entire match.
        last_dot_position = match.start()
        # Slice the string up to the dot and append the new extension
        new_file_name = file[:last_dot_position] + new_extension
    else:
        # No dot found, keep the original file name
        new_file_name = file
    return new_file_name
# rename_extension(file)

# file = r"C:\Users\ny4007991\OneDrive - Munich Re\Professional\Munich Re\Email Supp\File Processing\202407 July\MMG CC0363 June file attached\EQB0363BORD (17).xlsx"
def extract_file_name(file):
    r"""Regular expression to match the file name
    [^\\]: This is a character class that matches any character except a backslash (\). The ^ at the beginning of the character class negates the set, so it matches any character that is not in the set. Since backslash is an escape character in both Python strings and regular expressions, it needs to be escaped with another backslash. Hence, \\ represents a single backslash character in the context of a regular expression within a raw string.
    +: This quantifier matches one or more occurrences of the preceding element ([^\\] in this case). Combined with [^\\], it matches a sequence of characters that does not contain a backslash.
    $: This is an anchor that matches the end of the string. It ensures that the pattern matches only at the end of the string.
    """
    pattern = r'[^\\]+$'
    match = re.search(pattern, file)
    if match:
        # match.group() Method: The .group() method is used to access the part of the string where there was a match. By default, .group() without any arguments (or .group(0)) returns the entire match. If the pattern includes capturing groups (parts of the pattern enclosed in parentheses), you can pass an index to .group(index) to get the specific group. For example, .group(1) returns the first capturing group.
        file_name = match.group()
        # print(file_name)
    else:
        print("File name not found.")
    return file_name
