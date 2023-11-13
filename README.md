# Parse_nality_Cult

A grammar and parser for a stripped-down version of Python, as per the course requirements.

Files:
* Grammar files:
	* `PyParser.g4`
	* `PyLexer.g4`
* Parser: `parse.py`

## Team

* Dillon Jackson
* Matthew Kunze

## Usage

These instructions assume you're in a Unix environment (macOS/Linux), but it shouldn't be too different on Windows.

### Install requirements
```
pip install -r requirements.txt
```

### Build the grammar
```
./build.sh
```

### Run the parser

The following command will generate a parse tree and output the Lisp-style representation of it:

```
python3 parse.py input.py
```

### Show an image of the parse tree

The following command will generate and display an image of the parse tree for the provided input Python script:

```
./show_parse_tree.sh input.py
```

## Example

The following parse tree is produced for the deliverable 1 test case:

![](parse_tree_example.jpg)

[Direct link to image file (you'll need to use your browser's zoom tool)](https://raw.githubusercontent.com/Dailylulll/Parse_nality_Cult/main/parse_tree_example.jpg)
