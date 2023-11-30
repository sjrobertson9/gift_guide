# Contains functions for main.py
# @author Sarah Robertson
# @date 11.30.23

import items as i

# Current list of valid characters
names = ['alex', 'haley', 'sebastian', 'marnie', 'wizard']

# List of opinion + associated friendship points
values = {
    'love'    : '+80 FRIENDSHIP POINTS',
    'like'    : '+45 FRIENDSHIP POINTS',
    'neutral' : '+20 FRIENDSHIP POINTS',
    'dislike' : '-20 FRIENDSHIP POINTS',
    'hate'    : '-40 FRIENDSHIP POINTS'
}

# Whole shebang for checking gift opinion
def check(name, gift):
    # check for character exceptions
    opinion = which_name_exceptions(name, gift)
    if opinion is not None: # exception found
        value = values[opinion]
        print(gift, ":", opinion, value)
        print()
        return
    opinion = get_opinion(name, gift)
    if opinion is None: # not found
        print("not found! try again m'boy")
        print()
        return
    value = values[opinion]
    print(gift, ": ", opinion, value)
    print()

# Checks if the entered name belongs to a valid character
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

# Calls the relevant exception function
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

# Determines opinion for gift + character
def get_opinion(name, gift):
    ch_items = which_name_items(name)
    op = 'like' # opinion to be returned
    for key in ch_items:
        if isinstance(ch_items[key], list):
            for x in ch_items[key]:
                if gift in x:
                    return key
        else:
            if gift in ch_items[key]:
                return key
    return None # gift not found

# Returns the relevant dictionary
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

# Exceptions for Alex
def alex(gift):
    if 'void egg' in gift:
        return 'dislike'
    elif 'fruit tree fruit' in gift:
        return 'like'
    elif 'salmonberry' in gift or 'wild horseradish' in gift:
        return 'dislike'
    else: 
        return None

# Exceptions for Haley
def haley(gift):
    if 'prismatic shard' in gift or 'clay' in gift or 'wild horseradish' in gift or 'fish' in gift:
        return 'hate'
    elif 'vegetable' in gift or 'hops' in gift or 'tea leaves' in gift or 'wheat' in gift:
        return 'dislike'
    elif 'coconut' in gift or 'fruit salad' in gift or 'pink cake' in gift or 'sunflower' in gift:
        return 'love'
    
# Exceptions for Sebastian
def sebastian(gift):
    pass

# Exceptions for Marnie
def marnie(gift):
    pass

# Exceptions for Wizard
def wizard(gift):
    pass

# Just prints a silly end message and quits
def done():
    print()
    print("Thanks! Bye")
    print()
    exit()