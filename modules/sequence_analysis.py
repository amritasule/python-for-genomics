"""
Sequence Analysis Module
Advanced analysis functions for genomic sequences
"""

import sys
sys.path.append('../modules')
from dna_tools import gc_content


def find_motif(sequence, motif):
    """
    Find all occurrences of a motif in sequence.
    
    Args:
        sequence (str): DNA sequence to search
        motif (str): Motif pattern to find
        
    Returns:
        list: List of starting positions (0-indexed)
        
    Example:
        >>> find_motif("ATGATGATG", "ATG")
        [0, 3, 6]
    """
    positions = []
    start = 0
    
    while True:
        pos = sequence.find(motif, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
        
    return positions


def find_orfs(sequence):
    """
    Find all open reading frames (ORFs) in sequence.
    An ORF starts with ATG and ends with stop codon (TAA, TAG, TGA).
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        list: List of tuples (start_pos, end_pos, orf_sequence)
    """
    sequence = sequence.upper()
    orfs = []
    stop_codons = ['TAA', 'TAG', 'TGA']
    
    # Find all ATG positions
    start_positions = find_motif(sequence, 'ATG')
    
    for start in start_positions:
        for i in range(start + 3, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if codon in stop_codons:
                orf = sequence[start:i+3]
                orfs.append((start, i+3, orf))
                break
                
    return orfs


def calculate_melting_temp(sequence):
    """
    Calculate melting temperature using Wallace rule.
    Tm = 2(A+T) + 4(G+C)
    
    Args:
        sequence (str): DNA sequence
        
    Returns:
        float: Melting temperature in Celsius
    """
    sequence = sequence.upper()
    at = sequence.count('A') + sequence.count('T')
    gc = sequence.count('G') + sequence.count('C')
    
    return 2 * at + 4 * gc


def gc_content_window(sequence, window_size=100):
    """
    Calculate GC content in sliding windows.
    
    Args:
        sequence (str): DNA sequence
        window_size (int): Size of sliding window
        
    Returns:
        list: List of (position, gc_content) tuples
    """
    results = []
    
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        gc = gc_content(window)
        results.append((i, gc))
        
    return results


def hamming_distance(seq1, seq2):
    """
    Calculate Hamming distance between two sequences.
    (Number of positions where nucleotides differ)
    
    Args:
        seq1 (str): First sequence
        seq2 (str): Second sequence
        
    Returns:
        int: Hamming distance
        
    Example:
        >>> hamming_distance("ATGC", "AGGC")
        1
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be same length")
        
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))


def find_repeats(sequence, min_length=3):
    """
    Find repeated subsequences in a DNA sequence.
    
    Args:
        sequence (str): DNA sequence
        min_length (int): Minimum length of repeats to find
        
    Returns:
        dict: Dictionary of {repeat_sequence: count}
    """
    repeats = {}
    sequence = sequence.upper()
    
    for length in range(min_length, len(sequence) // 2 + 1):
        for i in range(len(sequence) - length + 1):
            subseq = sequence[i:i+length]
            count = sequence.count(subseq)
            if count > 1:
                repeats[subseq] = count
    
    return repeats


if __name__ == "__main__":
    # Test the functions
    test_seq = "ATGCGCTAGGGTAAATGCCCTAGATGATG"
    
    print("Testing Sequence Analysis Module")
    print("=" * 50)
    print(f"Sequence: {test_seq}")
    print(f"\nATG positions: {find_motif(test_seq, 'ATG')}")
    print(f"\nORFs found: {len(find_orfs(test_seq))}")
    for start, end, orf in find_orfs(test_seq):
        print(f"  Position {start}-{end}: {orf}")
    print(f"\nMelting temperature: {calculate_melting_temp(test_seq)}°C")
    print(f"\nHamming distance (ATGC vs AGGC): {hamming_distance('ATGC', 'AGGC')}")
