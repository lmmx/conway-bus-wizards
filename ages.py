# Let the set of children, X, be the class `AgeSet`
# Let the cardinality of the set of children be `AgeSet.n_children`
# Let the sum and product of the ages be `AgeSet.total` and `AgeSet.product`

# n_children > 1

from operator import mul
from functools import reduce


class AgeSet(object):
    def __init__(self, age_list):
        assert len(age_list) > 1, ValueError("Must give more than one age")
        age_int_check = all(map(lambda a: a == int, map(type, age_list)))
        assert age_int_check, TypeError("The ages provided are not all integers")
        self.ages = age_list
        return

    def __repr__(self):
        r = f"|X|={self.n_children}, X=({self.ages}), ΣX={self.total}"
        return r


    def __full_repr__(self):
        r = f"X=({self.ages}), ΣX={self.total}, ΠX={self.product}"
        return r

    @property
    def n_children(self):
        return len(self.ages)

    @property
    def total(self):
        return sum(self.ages)

    @property
    def product(self):
        return reduce(mul, self.ages)
