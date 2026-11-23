def to_rna(dna_strand):

    translation_map = {"G": "C", "C": "G", "T": "A", "A": "U"}

    rna_list = []

    for char in dna_strand:
        rna_list.append(translation_map[char])

    return "".join(rna_list)
