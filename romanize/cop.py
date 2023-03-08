#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: cop.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = True

data = OrderedDict()

# http://en.wikipedia.org/wiki/Coptic_alphabet

# letters from ⲁ to ⲑ (1 - 9)
# alef:http://en.wiktionary.org/wiki/
data["alpha"] = dict(
    letter=["ⲁ"], name="ⲁ", segment="vowel", subsegment="", transliteration="a", order=1
)
# beth:http://en.wiktionary.org/wiki/
data["beth"] = dict(
    letter=["ⲃ"],
    name="ⲃ",
    segment="consonant",
    subsegment="",
    transliteration="b",
    order=2,
)
# gimel:http://en.wiktionary.org/wiki/
data["gamma"] = dict(
    letter=["ⲅ"],
    name="ⲅ",
    segment="consonant",
    subsegment="",
    transliteration="g",
    order=3,
)
# daleth:http://en.wiktionary.org/wiki/
data["delta"] = dict(
    letter=["ⲇ"],
    name="ⲇ",
    segment="consonant",
    subsegment="",
    transliteration="d",
    order=4,
)
# he:http://en.wiktionary.org/wiki/
data["ei"] = dict(
    letter=["ⲉ"],
    name="ⲉי",
    segment="vowel",
    subsegment="",
    transliteration="e",
    order=5,
)
# vau:http://en.wikipedia.org/wiki/
data["so"] = dict(
    letter=["ⲋ"],
    name="ⲋ",
    segment="numeral",
    subsegment="",
    transliteration="w",
    order=6,
)
# zayin:http://en.wiktionary.org/wiki/
data["zeta"] = dict(
    letter=["ⲍ"],
    name="ⲍ",
    segment="consonant",
    subsegment="",
    transliteration="z",
    order=7,
)
# heth:http://en.wiktionary.org/wiki/
data["eta"] = dict(
    letter=["ⲏ"], name="ⲏ", segment="vowel", subsegment="", transliteration="ê", order=8
)
# teth:http://en.wiktionary.org/wiki/
data["theta"] = dict(
    letter=["ⲑ"],
    name="ⲑ",
    segment="consonant",
    subsegment="",
    transliteration="h",
    order=9,
)

# letters from י to ϥ (10 - 90)
# yod:http://en.wiktionary.org/wiki/
data["yota"] = dict(
    letter=["ⲓ"],
    name="ⲓ",
    segment="vowel",
    subsegment="",
    transliteration="i",
    order=10,
)
# kaph:http://en.wiktionary.org/wiki/
data["kappa"] = dict(
    letter=["ⲕ"],
    name="ⲕ",
    segment="consonant",
    subsegment="",
    transliteration="k",
    order=11,
)
# lamed:http://en.wiktionary.org/wiki/
data["lambda"] = dict(
    letter=["ⲗ"],
    name="ⲗ",
    segment="consonant",
    subsegment="",
    transliteration="l",
    order=12,
)
# mem:http://en.wiktionary.org/wiki/
data["me"] = dict(
    letter=["ⲙ"],
    name="ⲙ",
    segment="consonant",
    subsegment="",
    transliteration="m",
    order=13,
)
# num:http://en.wiktionary.org/wiki/
data["ne"] = dict(
    letter=["ⲛ"],
    name="ⲛ",
    segment="consonant",
    subsegment="",
    transliteration="n",
    order=14,
)
# samekh:http://en.wiktionary.org/wiki/
data["eksi"] = dict(
    letter=["ⲝ"],
    name="ⲝ",
    segment="consonant",
    subsegment="",
    transliteration="x",
    order=15,
)
# ayin:http://en.wiktionary.org/wiki/
data["o"] = dict(
    letter=["ⲟ"],
    name="ⲟ",
    segment="consonant",
    subsegment="",
    transliteration="o",
    order=16,
)
# pe:http://en.wiktionary.org/wiki/
data["pi"] = dict(
    letter=["ⲡ"],
    name="ⲡ",
    segment="consonant",
    subsegment="",
    transliteration="p",
    order=17,
)
# tsade:http://en.wikipedia.org/wiki/
data["fay"] = dict(
    letter=["ϥ"],
    name="ϥ",
    segment="numeral",
    subsegment="",
    transliteration="q",
    order=18,
)

# letters from ⲣ to ⳁ (100 - 900)
# resh:http://en.wiktionary.org/wiki/
data["ro"] = dict(
    letter=["ⲣ"],
    name="ⲣ",
    segment="consonant",
    subsegment="",
    transliteration="r",
    order=19,
)
# shin:http://en.wiktionary.org/wiki/
data["sima"] = dict(
    letter=["ⲥ"],
    name="ⲥ",
    segment="consonant",
    subsegment="",
    transliteration="s",
    order=20,
)
# tau:http://en.wiktionary.org/wiki/
data["taw"] = dict(
    letter=["ⲧ"],
    name="ⲧו",
    segment="consonant",
    subsegment="",
    transliteration="t",
    order=21,
)
# final_tsade:http://en.wiktionary.org/wiki/Tsade
data["epsilon"] = dict(
    letter=["ⲩ"],
    name="ⲩ",
    segment="vowel",
    subsegment="",
    transliteration="u",
    order=22,
)
# final_kaph:http://en.wiktionary.org/wiki/
data["fi"] = dict(
    letter=["ⲫ"],
    name="ⲫ",
    segment="consonant",
    subsegment="",
    transliteration="f",
    order=23,
)
# final_mem, chi:http://en.wiktionⲣary.org/wiki/
data["khe"] = dict(
    letter=["ⲭ"],
    name="ⲭ",
    segment="consonant",
    subsegment="",
    transliteration="c",
    order=24,
)
# final_nun:http://en.wiktionary.org/wiki/
data["epsi"] = dict(
    letter=["ⲯ"],
    name="ⲯ",
    segment="consonant",
    subsegment="",
    transliteration="y",
    order=25,
)
# final_pe:http://en.wiktionary.org/wiki/
data["ou"] = dict(
    letter=["ⲱ"],
    name="ⲱ",
    segment="vowel",
    subsegment="",
    transliteration="ô",
    order=26,
)
# final_tsade:http://en.wiktionary.org/wiki/Tsade
data["nine"] = dict(
    letter=["ⳁ"],
    name="ⳁ",
    segment="numeral",
    subsegment="",
    transliteration="j",
    order=27,
)

data["janja"] = dict(
    letter=["ϫ"],
    name="ϫ",
    segment="consonant",
    subsegment="",
    transliteration="č",
    order=28,
)

data["shai"] = dict(
    letter=["ϣ"],
    name="ϣ",
    segment="consonant",
    subsegment="",
    transliteration="š",
    order=29,
)
r = romanizer(data, has_capitals)

# collect coptic and transliteration letters from data dictionary for preprocessing function
letters = "".join(
    [
        "".join(d["letter"])
        + d["transliteration"]
        + "".join(d["letter"]).upper()
        + d["transliteration"].upper()
        for key, d in data.items()
    ]
)
regex = re.compile("[^%s ]+" % letters)
regex2 = re.compile(
    "[^%s\s]"
    % "".join(
        ["".join(d["letter"]) + "".join(d["letter"]).upper() for key, d in data.items()]
    )
)


def filter(string):
    """
    Preprocess string to remove all other characters but coptic ones

    :param string:
    :return:
    """
    # remove all unwanted characters
    return regex2.sub(" ", string)


def preprocess(string):
    """
    Preprocess string to transform all diacritics and remove other special characters

    :param string:
    :return:
    """
    return regex.sub("", string)


def convert(string, sanitize=False):
    """
    Swap characters from script to transliterated version and vice versa.
    Optionally sanitize string by using preprocess function.

    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))
