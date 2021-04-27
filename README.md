# treemaker.py

## About

This is a simple command-line interface for the tree parsing and drawing tools in the [nltk](http://www.nltk.org/) package. It is intended for instructors of and students in linguistics classes.

### Built with

- [nltk](http://www.nltk.org/)

If you do not have nltk installed, you will also need to [download additional data](https://www.nltk.org/data.html) after installing the python module. The `nltk-book` option is sufficient. 

## Getting started

Clone the repo locally. Run the file directly:

```python treemaker.py```

## Usage

By default, a basic context-free grammar based on the grammar from [*Language Files 12*](https://ohiostatepress.org/books/titles/9780814252703.html) is initialized, with an additional lexicon of terminals. Typing any sentence will display the trees for that sentence if they exist, and it will ask to learn any new words if they are not known. 

### Other commands

- `show grammar` Print the current grammar.
- `show category X` Show all productions whose lefthand side is X. 
- `add rule` Prompt for a new production to be added to the grammar.
- `save grammar` Saves the grammar to a file.
- `load grammar` Loads a grammar from a file.
- `reset grammar` Resets the grammar to the default CFG.
- `toggle latex` Toggles between nltk postscript output and LaTeX qtree text output. 
- `help`
- `quit` 

The format of the productions and grammars should follow that as those accepted by the `nltk.CFG.fromstring` function as described [here](http://www.nltk.org/book/ch08.html) and demonstrated below:

```
S -> NP VP
NP -> "cats" | "dogs"
VP -> "sleep"
```

## Contact

Nick Danis | nsdanis@wustl.edu | https://www.nickdanis.com/