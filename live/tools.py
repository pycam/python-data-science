def gc_content(seq):
    gc = 0
    for base in seq:
        if (base == 'G') or (base == 'C'):
            gc += 1
    return gc

def extract_seq(seq, window_size):
    results = []
    nb_windows = len(seq) - window_size + 1
    for i in range(nb_windows):
        results.append(seq[i:i+window_size])
    return results
