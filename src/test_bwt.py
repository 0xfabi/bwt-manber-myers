import pytest
from bwt import BwtManberMyers


def test_create_bucket():
    seq = "banana"
    bwt = BwtManberMyers(seq)
    stage = 1
    assert bwt._create_bucket([0, 1, 2, 3, 4, 5, 6], seq, stage) == {'b': [0], 'a': [1, 3, 5], 'n': [2, 4], '': [6]}

    seq = "abracadabra"
    bwt = BwtManberMyers(seq)
    stage = 1
    assert bwt._create_bucket([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], seq, stage) == {'a': [0, 3, 5, 7, 10], 'b': [1, 8], 'r': [2, 9], 'c': [4], 'd': [6], '': [11]}


def test_sort_manber_myers():
    seq = "banana"
    bwt = BwtManberMyers(seq)
    stage = 1
    suffixes_pos = [0, 1, 2, 3, 4, 5, 6]

    assert bwt._sort_manber_myers([0, 1, 2, 3, 4, 5, 6]) == [6, 5, 3, 1, 0, 4, 2]

    seq = "abracadabra"
    bwt = BwtManberMyers(seq)
    assert bwt._sort_manber_myers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]


def test_get_manber_myers_suffixes():
    seq = "banana"
    bwt = BwtManberMyers(seq)
    assert bwt._get_manber_myers_suffixes(seq) == [5, 3, 1, 0, 4, 2]

    seq = "abracadabra"
    bwt = BwtManberMyers(seq)
    assert bwt._get_manber_myers_suffixes(seq) == [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]


def test_get_bwt_seq():
    seq = "banana$"
    bwt = BwtManberMyers(seq)
    suffixes = [6, 5, 3, 1, 0, 4, 2]
    assert bwt._get_bwt_seq(seq, suffixes) == "annbaa"

    seq = "abracadabra$"
    bwt = BwtManberMyers(seq)
    suffixes = [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
    assert bwt._get_bwt_seq(seq, suffixes) == "ardrcaaaabb"


def test_transform():
    seq = "banana"
    bwt = BwtManberMyers(seq)
    assert bwt.transform() == "annbaa"

    seq = "abracadabra"
    bwt = BwtManberMyers(seq)
    assert bwt.transform() == "ardrcaaaabb"

    