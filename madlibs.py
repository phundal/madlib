#!/usr/bin/env python3

"""Madlibs for kids in elementary school """

import random
import json


def main():
    welcome = ['Pylibs - an interactive python version of madlibs!']

    print("\n".join(welcome))

    filename = 'bookofstories.json'

    with open(filename) as f_obj:
        bookofstories = json.load(f_obj)

    # setting up the play_again loop
    play_again = True

    while play_again:

        # pick a random story
        storynumber = input("\nPick a story number from 1 to " +
                            str(len(bookofstories)) + " or hit enter for a random one: ")
        if storynumber == '': # if the user wants a random story
            storynumber = random.randint(1, len(bookofstories))

        print("\nOk! We are going with story number: " + str(storynumber) + "\n\n")
        wordystory = bookofstories[str(storynumber)]

        # create an empty list to build the new madlib
        madlibs = []

        wordnum = 0
        storylength = len(wordystory)

        while wordnum < storylength:
            madlibs.append(wordystory[wordnum])
            wordnum = wordnum + 1
            if wordnum < storylength: # quickly check if there is an uneven number of entries
                word = wordystory[wordnum]
                madlib = input(word + ": ")
                madlibs.append(madlib)
                wordnum = wordnum + 1

        print("\n")
        print(''.join(madlibs))

        # Ask if they want more fun.
        play_again = False
        replay = input("\n \nWould you like to play again (y/n) ?")
        if replay == "y" or replay == "":
            play_again = True


if __name__ == "__main__":
    main()
