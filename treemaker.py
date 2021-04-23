import nltk
from nltk import CFG
from nltk.draw.tree import draw_trees
import re, sys

lf_string = """
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

lf_grammar = CFG.fromstring(lf_string)
parser = nltk.ChartParser(lf_grammar)

def parse_sentence(sentence):
    '''parses a string s and draws the trees'''
    parses = []
    try:
        for tree in parser.parse(sentence.split()):
            parses.append(tree)
        if parses == []:
            print("No trees found")
        else:
            print(f'I found {len(parses)} tree(s) for this sentence.')
            draw_trees(*parses)
    except Exception as e:
        print("Error!", e)
        new_words = re.findall(r'(?<=\')\w+(?=\')',str(e))
        print('Should I learn them?')
        reply = input()
        if reply == "yes":
            learn_words(new_words)
            parse_sentence(sentence)
        else:
            return
        
def update_parser():
    '''updates the grammar and parser'''
    global parser
    parser = nltk.ChartParser(lf_grammar)
    print("Grammar updated:\n",lf_grammar)
    return
    
def update_grammar(s,reset=False):
    '''updates the grammar as a raw string'''
    global lf_string, lf_grammar
    if reset:
        lf_string = ''
    lf_string += s
    lf_grammar = CFG.fromstring(lf_string)
    return

def show_productions(lhs):
    '''prints all productions for a given lhs as string'''
    for pr in lf_grammar.productions(lhs=nltk.grammar.Nonterminal(lhs)):
        print(pr)
    return

def learn_words(words):
    '''takes a list of words and adds the relevant productions to the grammar'''
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
        f.write(lf_string)
    print(f'Grammar saved as {filename}.')
    return

def load_grammar():
    '''loads a grammar from a text file directly as a grammar object'''
    global lf_grammar
    print("What is the name of the grammar?")
    filename = input()
    new_grammar = nltk.data.load(f'file:{filename}',format='cfg')
    lf_grammar = new_grammar
    update_parser()
    return

def show_category(s):
    '''show all productions with s as the lhs'''
    cats = lf_grammar.productions(lhs=nltk.grammar.Nonterminal(s))
    if cats == []:
        print('None found!')
    else:
        for p in cats:
            print(p)
    return
   

def main():
    print("Gimme a sentence:")
    user = input()
    if user == "show grammar":
        print(lf_grammar)
    elif re.match(r'(show category )(.*)',user):
        cat = re.match(r'(show category) (.*)',user).group(2)
        show_category(cat)
    elif user == "add rule":
        add_production()
    elif user == "save grammar":
        save_grammar()
    elif user == "load grammar":
        load_grammar()
    elif user == "quit":
        print("k bye")
        return
    else:
        parse_sentence(user)
    main()

main()