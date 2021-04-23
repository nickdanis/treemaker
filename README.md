# treemaker.py

## About

This is a simple interface for the tree parsing and drawing tools in the [nltk](http://www.nltk.org/) package. It is intended for instructors of and students in linguistics classes.

### Built with

- [nltk](http://www.nltk.org/)

## Getting started

Clone the repo locally. Run the script directly:

```python treemaker.py```

## Usage

By default, a basic context-free grammar based on the grammar from *Language Files 12* is initialized. Typing any sentence will display the trees for that sentence if they exist, and it will ask to learn any new words if they are not known. 

### Other commands

- `show grammar` Print the current grammar.
- `show category X` Show all productions whose lefthand side is X. 
- `add rule` Prompt for a new production to be added to the grammar.
- `save grammar` Saves the grammar to a file.
- `load grammar` Loads a grammar from a file.
- `reset grammar` Resets the grammar to the default CFG.
- `quit` 

The format of the productions and grammars should follow that for [nltk](http://www.nltk.org/book/ch08.html). 

## Contact

Nick Danis - nsdanis@wustl.edu