# can be used as a library, or a standalone script
# in script mode, it accepts a file to preprocess via stdin and outputs via stdout

import sys

# `script` is a string containing the Python script to preprocess
def preprocess(script):
    output = ""
    indent_stack = 0
    for line in script.split("\n"):
        tab_count = 0
        for char in line:
            if char == '\t':
                tab_count += 1
            else:
                break
        new_line = None
        if tab_count > indent_stack:
            indent_stack += 1
            new_line = "indent " + line[tab_count:]
        elif tab_count < indent_stack:
            new_line = line[tab_count:]
            for i in range(indent_stack - tab_count):
                new_line = "dedent " + new_line
                indent_stack -= 1
        else:
            new_line = line[tab_count:]
        output += new_line + "\n"
    while indent_stack > 0:
        output += "dedent\n"
        indent_stack -= 1
    return output

def main():
    script = sys.stdin.buffer.read().decode("utf-8")
    print(preprocess(script), end="")

if __name__ == "__main__":
    main()
