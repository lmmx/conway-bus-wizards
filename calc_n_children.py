from ages import AgeSet
from factor import all_factors, dedup_list

for A_w in range(1, 101):
    factored = all_factors(A_w)
    # tuples in the list `factored` will always be length 2 or more
    possible_agesets = [AgeSet(x) for x in factored]
    # Skip the primes, these do not admit more than one factorisation
    # A number is prime when it has only 1 possible factorisation
    # (the trivial factorisation of one and itself), check the value
    # of `[x for x in possible_agesets if len(x) == 1]` against OEIS:
    # https://oeis.org/A000040
    if len(possible_agesets) > 1:
        brood_size = [a.n_children for a in possible_agesets[1:]]
        if len(brood_size) > len(set(brood_size)):
            print(f"A_w = {A_w}:", sorted(brood_size))
