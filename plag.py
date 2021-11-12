# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:22:19 2021

@author: kaust
"""
import sys
import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


prog=sys.argv[0]
arg1=sys.argv[1]
arg2=sys.argv[2]
vector1 = text_to_vector(arg1)
vector2= text_to_vector(arg2)
cosine = get_cosine(vector1, vector2)
percentage="{:.3%}".format(cosine)

print("Cosine:", percentage)