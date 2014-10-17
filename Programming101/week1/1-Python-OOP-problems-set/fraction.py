"""
__lt__(self, other) # self < other
__gt__(self, other) # self > other
__add__(self, other) # self + other
__sub__(self, other) # self - other
__eq__(self, other) # self == other

"""
from fractions import *


class MyFraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        self.value = self.num / self.denom

    def __lt__(self, frac_one, frac_two):
        return frac_one.value < frac_two.value

    def __gt__(self, frac_one, frac_two):
        return frac_one.value > frac_two.value



a = MyFraction(3, 7)