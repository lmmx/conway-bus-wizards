def get_duplicates(dup_list):
    dedup_set = set(dup_list)
    copy_dup_list = list(dup_list)
    for x in dedup_set:
        del copy_dup_list[copy_dup_list.index(x)]
    return list(set(copy_dup_list))


def dedup_list(dup_list):
    """
    Remove rearrangements (permutations) by iterating through all the items in the
    list, storing each as a sorted list, then comparing the sorted form of every
    encountered one (as `visible`) against this `seen_set`.

    Used to deduplicate the flattened list returned from
    `factorise_further(without_rearrangements=True)`, as well as to deduplicate the
    total factorisation returned from `recursive_factorisation` in the body of the
    `all_factors` function.
    """
    seen_set = set()
    without_rearrangements = []
    for x in dup_list:
        visible = tuple(sorted(x))
        if visible not in seen_set:
            seen_set.add(visible)
            without_rearrangements.append(x)
    return without_rearrangements
