__author__ = "Nathan I. Budd"
__email__ = "nibudd@gmail.com"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__date__ = "17 Dec 2017"


def is_levidrome_pair(word1, word2):
    """Checks if the pair of words are levidromes.

    The number of nodes and the highest order of Chebyshev polynomial should be
    chosen such that M > N to ensure that the least squares operator is valid.

    args:
        word1: string
        word2: string

    returns:
        is_levidrome: boolean
    """
    is_levidrome = False

    if word1[::-1] == word2 and word1[::-1] != word1:
        is_levidrome = True

    return is_levidrome
