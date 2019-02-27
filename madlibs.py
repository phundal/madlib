#!/usr/bin/env python3

"""Hangman"""

import random
import json


def main():
    welcome = ['Pylibs - an interactive python version of madlibs!']

    print("\n".join(welcome))
    # load in stories
    # filename = 'wordsforstories.json'
    # with open(filename) as f_obj:
    #     stories = json.load(f_obj)

    # Select random story from stories

    # bookofstories = {"1": ["There once was a very fast ", "noun (gendered)", " who was really good at ",
    #                        "verb (present tense)", ". In fact ", "pronoun", " ", "verb (past tense)", " so much, he became a ", "noun (object)", ". "],
    #                  "2": ["There once was a very fast ", "noun (gendered)", " who was really good at ",
    #                        "verb (present tense)", ". In fact ", "pronoun", " ", "verb (past tense)", " so much, he became a ", "noun (object)", ". "],
    #                  "3": ["There once was a very fast ", "noun (gendered)", " who was really good at ",
    #                        "verb (present tense)", ". In fact ", "pronoun", " ", "verb (past tense)", " so much, he became a ", "noun (object)", ". "],
    #                  "4": ["There once was a very fast ", "noun (gendered)", " who was really good at ",
    #                        "verb (present tense)", ". In fact ", "pronoun", " ", "verb (past tense)", " so much, he became a ", "noun (object)", ". "]}

    # wordystory = ["There once was a very fast ", "noun (gendered)", " who was really good at ",
    #               "verb (present tense)", ". In fact ", "pronoun", " ", "verb (past tense)", " so much, he became a ", "noun (object)", ". "]

    # filename = 'wordsforstories.json'
    filename2 = 'bookofstories.json'

    # with open(filename, 'w') as f_obj:
    #    json.dump(wordystory, f_obj)

    # with open(filename2, 'w') as f_obj:
    #    json.dump(bookofstories, f_obj)

    # with open(filename) as f_obj:
    #     wordystory = json.load(f_obj)

    with open(filename2) as f_obj:
        bookofstories = json.load(f_obj)

    # setting up the play_again loop

    play_again = True
    while play_again:
        # set up the game loop
        # print("number of stories:")
        # print(len(bookofstories))

        # pick a random story
        storynumber = input("\nPick a story number from 1 to " +
                            str(len(bookofstories)) + " or hit enter for a random one: ")
        if storynumber == '':
            storynumber = random.randint(1, len(bookofstories))
        print("\nOk! We are going with story number: " + str(storynumber) + "\n\n")
        wordystory = bookofstories[str(storynumber)]

        # print("number of stories:")
        # print(len(bookofstories))
        madlibs = []

        wordnum = 0
        storylength = len(wordystory)
        while wordnum < storylength:
            madlibs.append(wordystory[wordnum])
            wordnum = wordnum + 1
            if wordnum < storylength:
                word = wordystory[wordnum]
                madlib = input(word + ": ")
                madlibs.append(madlib)
                wordnum = wordnum + 1

        print("\n")
        print(''.join(madlibs))

        # Figure out if they want to go again.
        play_again = False
        replay = input("\n \nWould you like to play again (y/n) ?")
        if replay == "y":
            play_again = True


if __name__ == "__main__":
    main()
