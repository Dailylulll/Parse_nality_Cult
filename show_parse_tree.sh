if [ $# -ne 1 ]; then
	echo "usage: show_parse_tree.sh PYTHON_FILE"
	exit 1
fi

antlr4-parse PyLexer.g4 PyParser.g4 program -gui < "$1"