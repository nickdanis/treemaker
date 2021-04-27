import nltk
from nltk import CFG
from nltk.draw.tree import draw_trees
import re

def parse_sentence(sentence):
    '''parses a string s and draws the trees'''
    parses = []
    try:
        for tree in parser.parse(sentence.split()):
            parses.append(tree)
        if parses == []:
            print("This sentence is ungrammatical.")
        else:
            print(f'I found {len(parses)} tree(s) for this sentence.')
            if latex:
                for tree in parses:
                    print(tree.pformat_latex_qtree())
            else:
                draw_trees(*parses)
    except Exception as e:
        print("Error!", e)
        new_words = re.findall(r'(?<=\')\w+(?=\')',str(e))
        print('Should I learn them? (y/n)')
        reply = input()
        if reply == "y":
            learn_words(new_words)
            parse_sentence(sentence)
        else:
            return

def toggle_latex():
    global latex
    latex = not latex
    if latex:
        print("LaTeX output enabled")
    else:
        print("LaTeX output disabled")
    return
        
def update_parser():
    '''updates the grammar and parser'''
    global parser
    parser = nltk.ChartParser(grammar)
    print(f"Grammar updated with {len(grammar.productions())} total productions.")
    return
    
def update_grammar(s,reset=False):
    '''updates the grammar as a raw string'''
    global grammar_raw, grammar
    if reset:
        grammar_raw = ''
    grammar_raw += s
    grammar = CFG.fromstring(grammar_raw)
    return

def show_productions(lhs):
    '''prints all productions for a given lhs as string'''
    for pr in grammar.productions(lhs=nltk.grammar.Nonterminal(lhs)):
        print(pr)
    return

def learn_words(words):
    '''takes a list of words and adds the relevant productions to the grammar'''
    words = list(set(words))
    new_rules = ""
    for w in words:
        print(f'What is the category of {w}?')
        category = input()
        new_rules += f"\n{category} -> '{w}'"
    update_grammar(new_rules)
    update_parser()
    return
    
def add_production():
    '''adds a production the the string from the user'''
    print("Enter a new rule:")
    production = input()
    update_grammar("\n"+production)
    update_parser()
    return

def save_grammar():
    '''saves grammar to a text file'''
    print("Give a name:")
    name = input()
    filename = name + '.cfg'
    with open(filename, 'w') as f:
        f.write(grammar_raw)
    print(f'Grammar saved as {filename}.')
    return

def load_grammar():
    '''loads a grammar from a text file directly as a grammar object'''
    global grammar
    print("What is the name of the grammar?")
    filename = input()
    new_grammar = nltk.data.load(f'file:{filename}',format='cfg')
    grammar = new_grammar
    update_parser()
    return

def show_category(s):
    '''show all productions with s as the lhs'''
    cats = grammar.productions(lhs=nltk.grammar.Nonterminal(s))
    if cats == []:
        print('Category not found.')
    else:
        for p in cats:
            print(p)
    return

def reset_grammar():
    '''resets the grammar to the default LF cfg'''
    update_grammar(lf_raw,reset=True)
    update_parser()
    return

def show_grammar():
    '''prints the current grammar'''
    print(grammar)
    return

def main():
    print("Gimme a sentence:")
    user = input()
    if re.match(r'(show category )(.*)',user):
        cat = re.match(r'(show category) (.*)',user).group(2)
        show_category(cat)
    elif user in dispatch:
        dispatch[user]()
    elif user == "quit":
        print("bye!")
        return
    else:
        parse_sentence(user)
    main()

dispatch = {
    "add rule" : add_production,
    "save grammar" : save_grammar,
    "load grammar" : load_grammar,
    "reset grammar" : reset_grammar,
    "toggle latex" : toggle_latex,
    "show grammar" : show_grammar
}

lf_raw = """
S -> NP VP
NP -> Det N
VP -> TV NP | DTV NP NP | SV S 
PP -> P NP
N -> 'cat' | 'dog' | 'professor' | 'student' | 'computer'
Det -> 'the' | 'a' | 'their'
Adj -> 'sleepy' | 'energetic'
Adv -> 'yesterday' | 'easily'
TV -> 'photographed' | 'saw'
DTV -> 'gave' | 'sent'
SV -> 'said'
P -> 'in' | 'at' | 'with' | 'for' | 'on'
N -> N PP
N -> Adj N 
VP -> VP Adv | VP PP
"""

# set the initial grammar to the predefined LF grammar above
grammar_raw = lf_raw

# build the grammar and parser objects from nltk
grammar = CFG.fromstring(grammar_raw)
parser = nltk.ChartParser(grammar)
latex = False

main()