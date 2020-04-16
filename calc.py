from ages import AgeSet
from factor import all_factors
from duplication import get_duplicates


for A_w in range(1, 1001):
    factored = all_factors(A_w)
    # tuples in the list `factored` will always be length 2 or more
    possible_agesets = [AgeSet(x) for x in factored]
    # Skip the primes, these do not admit more than one factorisation
    # A number is prime when it has only 1 possible factorisation
    # (the trivial factorisation of one and itself), check the value
    # of `[x for x in possible_agesets if len(x) == 1]` against OEIS:
    # https://oeis.org/A000040
    if len(possible_agesets) > 1:
        # Maybe remove the no trivial factorisation condition later
        # i.e. take off the slice at the end of the following line:
        poss_brood_sizes = [a.n_children for a in possible_agesets[1:]]
        if len(poss_brood_sizes) > len(set(poss_brood_sizes)):
            # There is duplication: multiple |X| for the given A_w
            dup_sizes = get_duplicates(poss_brood_sizes)
            for poss_size in dup_sizes:
                all_dupsized_agesets = [a for a in possible_agesets[1:] if a.n_children == poss_size]
                totals = [a.total for a in all_dupsized_agesets]
                dup_totals = get_duplicates(totals)
                if len(dup_totals) < 1:
                    # Looking for agesets with duplicated sums
                    continue
                for a_s in all_dupsized_agesets:
                    if a_s.total in dup_totals:
                        print(f"A_w = {A_w}:", a_s)
                print()
