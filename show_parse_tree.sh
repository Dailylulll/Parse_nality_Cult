#!/bin/bash

if [ $# -ne 1 ]; then
	echo "usage: show_parse_tree.sh PYTHON_FILE"
	exit 1
fi

p_script=$(python3 preprocessor.py < "$1")
printf '%s' "$p_script" | antlr4-parse PyLexer.g4 PyParser.g4 program -gui
