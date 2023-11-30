# Contains functions for main.py
# @author Sarah Robertson
# @date 11.30.23

import items as i

names = ['alex', 'haley', 'sebastian', 'marnie', 'wizard']

values = {
    'love'    : '+80 FRIENDSHIP POINTS',
    'like'    : '+45 FRIENDSHIP POINTS',
    'neutral' : '+20 FRIENDSHIP POINTS',
    'dislike' : '-20 FRIENDSHIP POINTS',
    'hate'    : '-40 FRIENDSHIP POINTS'
}

def check(name, gift):
    # check for character exceptions
    opinion = which_name_exceptions(name, gift)
    if opinion is not None: # exception found
        value = values[opinion]
        print(gift, ":", opinion, value)
        print()
        return
        
    opinion = get_opinion(name, gift)
    print(gift, ": ", value)

def check_name(name):
    if name in names:
        return True
    else:
        print()
        print("Character not found!")
        print()
        print("Usage:", names)
        print()
        return False
    
def which_name_exceptions(name, gift):
    if name == ('alex'):
        return alex(gift)
    elif name == ('haley'):
        return haley(gift)
    elif name == ('sebastian'):
        return sebastian(gift)
    elif name == ('marnie'):
        return marnie(gift)
    elif name == ('wizard'):
        return wizard(gift)

def get_opinion(name, gift):
    ch_items = which_name_items(name)

def which_name_items(name):
    if name == ('alex'):
        return i.alex
    elif name == ('haley'):
        return i.haley
    elif name == ('sebastian'):
        return i.sebastian
    elif name == ('marnie'):
        return i.marnie
    elif name ==('wizard'):
        return i.wizard

def alex(gift):
    if 'void egg' in gift:
        return 'dislike'
    elif 'fruit tree fruit' in gift:
        return 'like'
    elif 'salmonberry' in gift or 'wild horseradish' in gift:
        return 'dislike'
    else: 
        return None

def haley(gift):
    pass

def sebastian(gift):
    pass

def marnie(gift):
    pass

def wizard(gift):
    pass

def done():
    print()
    print("Thanks! Bye")
    print()
    exit()