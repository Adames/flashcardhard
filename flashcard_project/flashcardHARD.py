from os import remove
from sys import exit
from random import shuffle
from os.path import exists, getsize

"""
This program allows you to make, learn, and delete decks of flashcards.
"""

text_frame = '-' * 37 + '{DECK}' + '-' * 37
linebreak = '\n' + ('-+' * 40) + '\n'
welcome = '\n' + '/\\' * 40 + "\n\n\t\t\t\tflashcardHARD\n\n" + '\/' * 40
flashcards = []

def start():
  print welcome
  menu()

def menu():
  """ This function opens the main menu. """
  print linebreak
  print """\rWelcome to flashcardHARD! You're here because you don't know:
  \rI'm here to make you learn it. Let's get started.\n
  \r1) Write a deck
  \r2) Test a deck
  \r3) Kill a deck
  \r4) Exit\n
  \rSelect option 1, 2, 3, or 4:"""
  menu_item = raw_input('> ')
  if menu_item == '1':
    write_menu()
  elif menu_item == '2':
    learn_menu()
  elif menu_item == '3':
    kill_menu()
  elif menu_item == '4':
    exit(0)
  else:
    print "I've got just the deck for you: \"Typing for Dummies.\""
    print "Try again"
  menu()

def write_menu():
  """ This function allows the user to name a deck, checks if it exists,
  then allows them to remake the deck are select a new deck name.
  Does not build the deck.
  """
  print linebreak
  print "What would you like to call your deck?"
  print "(To return to the menu, type \"menu\")"
  deck_name = raw_input('> ')
  if deck_name == 'menu':
    menu()
  elif exists(deck_name):
    print """
    \rThis deck already exists. What would you like to do?\n
    \r1)Erase %s and create a new file called %s or
    \r2)Use a different deck name
    \r(To return to the menu, type "menu")""" % (deck_name, deck_name)
    deck_exists = raw_input('> ')
    if deck_exists == 'menu':
      menu()
    elif deck_exists == '1':
      print linebreak
      build_list(deck_name)
    elif deck_exists == '2':
      write_menu()
    else:
      print "I've got just the deck for you: \"Typing for Dummies.\""
      print "Try again"
      menu()
  elif not exists(deck_name):
    build_list(deck_name)
  else:
    print "I've got just the deck for you: \"Typing for Dummies.\""
    print "Try again"
    menu()

def build_list(deck_name):
  """This function creates a list so we can build a deck"""
  print "\nMake a flashcard! When you are finished, simply type 'done' into the prompt."
  print "(To return to the menu, type \"menu\")"
  side1 = raw_input("Front side: ")
  if side1 == 'menu':
    menu()
  elif side1 == 'done':
    build_deck(deck_name)
  else:
    side2 = raw_input("Back side: ")
    # This is the string storage format
    flashcard = side1 + ': ' + side2
    keep_card = raw_input("""\nIs this correct?\n[%s]
                \rKeep it? (Y/N)\n""" % flashcard)
    kept_card = keep_card.lower()
    if kept_card == 'y':
      flashcards.append(flashcard)
      build_list(deck_name)
    elif kept_card == 'n':
      build_list(deck_name)
    else:
      print 'Invalid selection.'
      build_list(deck_name)

def build_deck(deck_name):
  """ Builds a deck by converting the flashcard list into a string. """
  make_deck = open(deck_name, 'w')
  # This line joins the list into a clean string
  flash_list = '\n'.join(flashcards)
  make_deck.write(flash_list)
  make_deck.close()
  print "\nDeck %s created. Moving to main menu." % deck_name
  menu()

def learn_menu():
  """ This function allows the user to pick a deck, checks if it exists,
  then send them to the correct learn/edit function.
  """
  print linebreak
  print "Which deck would you like to use?"
  print "(To return to the menu, type \"menu\")"
  deck_name = raw_input('> ')
  if deck_name == 'menu':
    menu()
  elif not exists(deck_name):
    print """
    \rThe deck %s does not exist. Would you like to:
    \r1) Create a deck named %s or
    \r2) Use a different deck?
    """ % (deck_name, deck_name)
    new_file = raw_input('> ')
    if new_file == '1':
      build_deck(new_file)
      print linebreak
    elif new_file == '2':
      learn_menu()
    else:
      print "I've got just the deck for you: \"Typing for Dummies.\""
      print "Try again"
      menu()
  elif exists(deck_name):
    learn_options(deck_name)
  else:
    print "I've got just the deck for you: \"Typing for Dummies.\""
    print "Try again"
    menu()
    
def clean_list_items(item):
  item = str(item)
  item1, item2 = item.strip('[\'\']').split(': ')
  return item1, item2

def learn_options(deck_name):
  """ This function takes the document, converts it into a list,
    then either tests users on it or reviews the list for them.
  """
  # This opens the file and converts it into a list.
  listed_deck = [l.split('\n') for l in open(deck_name)]
  print """
  \rWhat would you like to do with your deck?
  \r(type 'menu' to return to the main menu)
  \r1) Test me on my deck
  \r2) Review my deck"""
  use_option = raw_input('> ')
  if use_option == 'menu':
    menu()
  elif use_option == '1':
    print text_frame + "Shuffling deck for testing purposes..." + '\n'
    test_deck = shuffle(listed_deck)
    for cards in test_deck:
      side1, side2 = clean_list_items(cards)
      raw_input(side1 + ': ???' + '\n(Press any key for the answer below)')
      print side2 + '\n'
    print text_frame
    learn_options(deck_name)
  elif use_option == '2':
    open_deck = open(deck_name, 'r+')
    print "This is your deck:"
    print text_frame
    card_num = 0
    for flashcards in listed_deck:
      card_num += 1
      print "Card #%d: %s" % (card_num, flashcards)
    print text_frame
    learn_options(deck_name)
  else:
    print "I've got just the deck for you: \"Typing for Dummies.\""
    print "Try again"
    menu()

def kill_menu():
  print linebreak
  print "Which deck would you like to delete?"
  print "(type 'menu' to return to the main menu)"
  kill_deck = raw_input('> ')
  if kill_deck == 'menu':
    menu()
  elif not exists(kill_deck):
    print "The deck %s doesn't exist." % kill_deck
    kill_menu()
  elif exists(kill_deck):
    print "Are you sure you want to delete %s?" % kill_deck
    delete_action = raw_input('\n(Y/N)\n> ')
    if delete_action =='Y' or delete_action == 'y':
      remove(kill_deck)
      print "Deleting File."
      menu()
    else:
      print "Returning to menu."
      menu()
  else:
    print "I've got just the deck for you: \"Typing for Dummies.\""
    print "Try again"
    menu()
start()  
