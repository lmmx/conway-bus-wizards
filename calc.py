from ages import AgeSet
from factor import all_factors

for A_w in range(1,101):
    factored = all_factors(A_w)
    # tuples in the list `factored` will always be length 2 or more
    if len(factored) > 1:
        possible_agesets = [AgeSet(x) for x in factored]
