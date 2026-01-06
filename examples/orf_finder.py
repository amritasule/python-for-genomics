"""
Open Reading Frame (ORF) Finder
Find and analyze potential genes in DNA sequences
"""

import sys
sys.path.append('../modules')

import dna_tools
import sequence_analysis


def find_and_analyze_orfs(sequence, min_length=30):
    """
    Find all ORFs and analyze them.
    
    Args:
        sequence (str): DNA sequence
        min_length (int): Minimum ORF length to report
    """
    print(f"Searching for ORFs in {len(sequence)}bp sequence...")
    print(f"Minimum ORF length: {min_length}bp\n")
    
    orfs = sequence_analysis.find_orfs(sequence)
    
    # Filter by length
    long_orfs = [(start, end, orf) for start, end, orf in orfs if len(orf) >= min_length]
    
    print(f"Found {len(orfs)} total ORFs")
    print(f"Found {len(long_orfs)} ORFs >= {min_length}bp\n")
    
    if not long_orfs:
        print("No ORFs found meeting criteria")
        return
    
    print("="*70)
    for i, (start, end, orf) in enumerate(long_orfs, 1):
        protein = dna_tools.translate(orf)
        gc = dna_tools.gc_content(orf)
        
        print(f"\nORF #{i}")
        print(f"Position: {start}-{end} ({len(orf)}bp)")
        print(f"DNA: {orf}")
        print(f"Protein ({len(protein)}aa): {protein}")
        print(f"GC Content: {gc:.1f}%")
        print(f"Start codon: {orf[:3]}")
        print(f"Stop codon: {orf[-3:]}")
        print("-"*70)


def compare_reading_frames(sequence):
    """
    Compare ORFs in all three reading frames.
    """
    print("\nComparing all three reading frames:\n")
    
    for frame in range(3):
        frame_seq = sequence[frame:]
        orfs = sequence_analysis.find_orfs(frame_seq)
        
        print(f"Reading Frame +{frame+1}:")
        print(f"  ORFs found: {len(orfs)}")
        
        if orfs:
            longest = max(orfs, key=lambda x: len(x[2]))
            print(f"  Longest ORF: {len(longest[2])}bp at position {longest[0]+frame}")
        print()


if __name__ == "__main__":
    print("OPEN READING FRAME FINDER")
    print("="*70)
    
    # Example 1: Simple sequence with ORFs
    print("\nEXAMPLE 1: Finding ORFs")
    print("-"*70)
    
    test_sequence = "AAATGCGCGCGTAGGGTAAATGATGCCCCCCTAG"
    find_and_analyze_orfs(test_sequence, min_length=9)
    
    # Example 2: Longer sequence
    print("\n\nEXAMPLE 2: Longer Sequence Analysis")
    print("-"*70)
    
    long_sequence = (
        "ATGAAACGCATTAGCGCATAGGGGTAAGGGATG"
        "CGCGCGTAGCGTAGCTAGCGTAGGGTAAATGCCC"
        "ATGATGATGCGCGCGTAGCGTAGCTAGCGTAGGG"
    )
    
    find_and_analyze_orfs(long_sequence, min_length=15)
    
    # Example 3: Compare reading frames
    print("\n\nEXAMPLE 3: Reading Frame Comparison")
    print("-"*70)
    
    compare_reading_frames(long_sequence)
    
    print("\n" + "="*70)
    print("Analysis complete!")
