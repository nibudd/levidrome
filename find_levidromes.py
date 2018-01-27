__author__ = "Nathan I. Budd"
__email__ = "nibudd@gmail.com"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__date__ = "17 Dec 2017"


def load_words():

    import json
    import os

    try:
        filename = (os.path.dirname(os.path.realpath(__file__)) +
                    "/english-words/words_dictionary.json")
        with open(filename, "r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


def is_levidrome_pair(word1, word2):
    is_levidrome = False

    if word1[::-1] == word2 and word1[::-1] != word1:
        is_levidrome = True

    return is_levidrome


def find_levidromes():
    all_words = load_words()
    levidromes = []
    for word, v in all_words.items():
        drow = word[::-1]
        if (drow in all_words) and (word != drow) and (word not in levidromes):
            levidromes += [word, drow]

    levidrome_pairs = int(len(levidromes)/2)
    print("There are {} levidrome pairs.".format(levidrome_pairs))
    choice = input('Want to see them? ([y]/n): ')

    if choice != 'n':
        for pair in range(levidrome_pairs):
            i = pair*2
            print("{}({}/{}), ".format(pair+1
                                       , levidromes[i], levidromes[i+1]),
                  end='')


if __name__ == '__main__':
    find_levidromes()
