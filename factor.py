from itertools import chain, product as combine
from duplication import dedup_list


def all_factors(n):
    initial_factorisation = factorise(n)
    total_factorisation = list(chain(*recursive_factorisation(initial_factorisation)))
    return initial_factorisation + dedup_list(total_factorisation)


def recursive_factorisation(initial_factorisation):
    for i_f in initial_factorisation:
        subfactorisation = factorise_further(i_f, expand=True, rearrangements=False)
        if initial_factorisation != subfactorisation:
            subfactor_list = [f for f in subfactorisation if f != i_f]
            if len(subfactor_list) > 0:
                yield subfactor_list
                yield from recursive_factorisation(subfactor_list)


def factorise(n, nontrivial_only=False):
    """
    Return all pairs of factors. If `nontrivial_only` is True, omit the trivial
    factorisation of `n` into `(1,n)`.
    """
    assert type(n) is int, TypeError(f"{n} is not an integer")
    factorisations = [(i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    if nontrivial_only:
        factorisations = list(filter(lambda f: 1 not in f, factorisations))
    return factorisations


def factorise_further(factor_tuple, expand=False, rearrangements=True):
    """
    Given an initial factorisation, `factor_tuple`, find all pairs of factors
    returned by `factorise(n)` for each factor `n` in `factor_tuple`.

    Note: this function is to be passed one tuple representing a factorisation,
    not a list of tuples representing multiple possible factorisations!

    Having enumerated the pairs of factors, either there will be only the trivial
    factorisation of {1,n} (i.e. n is prime) or `n` will admit further factorisations.

    If a factor `n` can be factored further, then enumerate all of these factors as a
    list (that list may then be factored further, and so on).

    This function will return the lists of further factorisations for each of the
    integers given in the tuple `factor_tuple`.

    E.g. given (1,1)   ==>   [[1], [1]]
               (1,2)   ==>   [[1], [2]]
               (1,4)   ==>   [[1], [4, (2,2)]]
               (4,4)   ==>   [[4, (2,2)], [4, (2,2)]]
               (4,5)   ==>   [[4, (2,2)], [5]]
               ...

    and so on.

    If `expand` is True (default: False), these will be expanded out to the list of
    all possible combinations (i.e. all possible factorisations) using the
    `itertools.product` function (which is imported under the alias `combine`).

    E.g. given (1,1)   ==>   [(1, 1)]
               (1,2)   ==>   [(1, 2)]
               (1,4)   ==>   [(1, 4), (1, 2, 2))]
               (4,4)   ==>   [(4, 4), (4, 2, 2), (2, 2, 4), (2, 2, 2, 2)]
               (4,5)   ==>   [(4, 5), (2, 2, 5)]
               ...

    If `rearrangements` is False (default: True), rearrangements will not removed
    from the results. In the previous example, shown for `rearrangements` as True,
    for example the line for `(4,4)` contains both `(4,2,2)` and `(2,2,4)`, arising
    by splitting the first 4 and the second 4 into `(2,2)` before flattening the
    list. Below are the same examples for `rearrangements` set to False.

    E.g. given (1,1)   ==>   [(1, 1)]
               (1,2)   ==>   [(1, 2)]
               (1,4)   ==>   [(1, 4), (1, 2, 2)]
               (4,4)   ==>   [(4, 4), (4, 2, 2), (2, 2, 2, 2)]
               (4,5)   ==>   [(4, 5), (2, 2, 5)]
               ...

    
    Note that you can get infinitely many factorisations if you permit 1 to be factored
    into (1,1) i.e. [1, (1,1), (1,1,1), (1,1,1,1), ...] so primes are not factored into
    the trivial factorisation and just kept as single integers.
    
    The lists returned by this function will be of the same length as the input tuple,
    and will always have as their first entry integer at the corresponding index of
    this input tuple (i.e. it will return a list of only this integer, n, or a list
    beginning with the integer, n, followed by tuples representing factorisations of
    that integer, n).
    """
    complete_factorisations = []
    for n_in_tuple, factor in enumerate(factor_tuple):
        extra_factorisations = [factor]  # extra factorisations will be appended later
        initial_factorisations = factorise(factor, nontrivial_only=True)
        # This loop will be skipped if `factor` admits only the trivial factorisation:
        for factorisation in initial_factorisations:
            extra_factorisations.append(factorisation)
        complete_factorisations.append(extra_factorisations)
    if expand:
        all_factorisations = list(combine(*complete_factorisations))
        all_factorisations_flattened = []
        for comb in all_factorisations:
            flat = chain.from_iterable([[a] if type(a) == int else a for a in comb])
            all_factorisations_flattened.append(tuple(flat))
        if rearrangements:
            return all_factorisations_flattened
        else:
            without_rearrangements = dedup_list(all_factorisations_flattened)
            return without_rearrangements
    else:
        return complete_factorisations
