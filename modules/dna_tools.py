"""
DNA Tools Module
Collection of functions for DNA sequence manipulation and analysis
"""

def validate_dna(sequence):
    """
    Check if sequence contains only valid DNA bases (A, T, G, C).
    
    Args:
        sequence (str): DNA sequence to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> validate_dna("ATGC")
        True
        >>> validate_dna("ATXC")
        False
    """
    valid_bases = set('ATGCatgc')
    return set(sequence).issubset(valid_bases)


def gc_content(sequence):
    """
    Calculate GC content percentage.
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        float: GC content as percentage
        
    Example:
        >>> gc_content("ATGC")
        50.0
    """
    if not sequence:
        return 0.0
    
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    return (g_count + c_count) / len(sequence) * 100


def at_content(sequence):
    """
    Calculate AT content percentage.
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        float: AT content as percentage
    """
    return 100 - gc_content(sequence)


def complement(sequence):
    """
    Get complement of DNA sequence.
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        str: Complement sequence
        
    Example:
        >>> complement("ATGC")
        'TACG'
    """
    complement_map = {
        'A': 'T', 'T': 'A', 
        'G': 'C', 'C': 'G',
        'a': 't', 't': 'a',
        'g': 'c', 'c': 'g'
    }
    
    return "".join([complement_map.get(base, base) for base in sequence])


def reverse_complement(sequence):
    """
    Get reverse complement of DNA sequence.
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        str: Reverse complement sequence
        
    Example:
        >>> reverse_complement("ATGC")
        'GCAT'
    """
    return complement(sequence)[::-1]


def transcribe(dna_sequence):
    """
    Transcribe DNA to RNA (replace T with U).
    
    Args:
        dna_sequence (str): DNA sequence
        
    Returns:
        str: RNA sequence
        
    Example:
        >>> transcribe("ATGC")
        'AUGC'
    """
    return dna_sequence.replace('T', 'U').replace('t', 'u')


def count_nucleotides(sequence):
    """
    Count occurrences of each nucleotide.
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        dict: Count of each nucleotide
        
    Example:
        >>> count_nucleotides("ATGCATGC")
        {'A': 2, 'T': 2, 'G': 2, 'C': 2}
    """
    sequence = sequence.upper()
    return {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }


def has_start_codon(sequence):
    """
    Check if sequence contains start codon (ATG).
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        bool: True if contains ATG, False otherwise
    """
    return 'ATG' in sequence.upper()


def has_stop_codon(sequence):
    """
    Check if sequence contains any stop codon (TAA, TAG, TGA).
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        bool: True if contains stop codon, False otherwise
    """
    sequence = sequence.upper()
    stop_codons = ['TAA', 'TAG', 'TGA']
    return any(codon in sequence for codon in stop_codons)


def translate(dna_sequence):
    """
    Translate DNA sequence to protein.
    
    Args:
        dna_sequence (str): DNA sequence (length must be multiple of 3)
        
    Returns:
        str: Amino acid sequence
        
    Example:
        >>> translate("ATGGCC")
        'MA'
    """
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
    
    dna_sequence = dna_sequence.upper()
    protein = ""
    
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if len(codon) == 3:
            protein += codon_table.get(codon, 'X')
        
    return protein


if __name__ == "__main__":
    # Test the functions
    test_seq = "ATGCGCTAGGGTAA"
    
    print("Testing DNA Tools Module")
    print("=" * 50)
    print(f"Sequence: {test_seq}")
    print(f"Valid DNA: {validate_dna(test_seq)}")
    print(f"GC Content: {gc_content(test_seq):.2f}%")
    print(f"AT Content: {at_content(test_seq):.2f}%")
    print(f"Complement: {complement(test_seq)}")
    print(f"Reverse Complement: {reverse_complement(test_seq)}")
    print(f"RNA: {transcribe(test_seq)}")
    print(f"Nucleotide counts: {count_nucleotides(test_seq)}")
    print(f"Has start codon: {has_start_codon(test_seq)}")
    print(f"Has stop codon: {has_stop_codon(test_seq)}")
    print(f"Translation: {translate(test_seq)}")
