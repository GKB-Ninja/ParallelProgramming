def remove_duplicates(seq: list) -> list:
    res = set(seq)
    return res

def list_counts(seq : list) -> dict:
    counts = {}
    for i in seq:
        counts[i] = counts.get(i,0) + 1
    return counts

def reverse_dict(d: dict) -> dict: 
    res = dict(reversed(list(d)))   
    return res
