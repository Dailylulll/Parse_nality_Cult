import sys

if len(sys.argv) != 2:
    print("usage: parse.py FILE")
    sys.exit(1)

fp = sys.argv[1]

indent_stack = 0
with open(fp, 'r') as infile:
    with open('tmp.txt', 'w') as outfile:
        for line in infile:
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
            outfile.write(new_line)