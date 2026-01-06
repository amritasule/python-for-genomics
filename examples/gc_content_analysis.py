"""
GC Content Analysis Example
Calculate and visualize GC content across sequences
"""

import sys
sys.path.append('../modules')

import dna_tools
import sequence_analysis


def analyze_gc_content(sequence, window_size=20):
    """
    Analyze GC content with sliding window.
    
    Args:
        sequence (str): DNA sequence
        window_size (int): Size of sliding window
    """
    print(f"Sequence length: {len(sequence)} bp")
    print(f"Overall GC content: {dna_tools.gc_content(sequence):.2f}%")
    print(f"\nGC content in {window_size}bp windows:\n")
    
    windows = sequence_analysis.gc_content_window(sequence, window_size)
    
    # Print first 10 windows
    for i, (pos, gc) in enumerate(windows[:10]):
        window_seq = sequence[pos:pos+window_size]
        bar = '█' * int(gc / 2)  # Visual representation
        print(f"Position {pos:4d}: {gc:5.1f}% {bar} {window_seq}")
    
    if len(windows) > 10:
        print(f"... ({len(windows) - 10} more windows)")
    
    # Find GC-rich regions (>60%)
    gc_rich = [(pos, gc) for pos, gc in windows if gc > 60]
    if gc_rich:
        print(f"\nGC-rich regions (>60%):")
        for pos, gc in gc_rich[:5]:
            print(f"  Position {pos}: {gc:.1f}%")


def compare_sequences(seq1, seq2, name1="Sequence 1", name2="Sequence 2"):
    """
    Compare GC content between two sequences.
    """
    gc1 = dna_tools.gc_content(seq1)
    gc2 = dna_tools.gc_content(seq2)
    
    print(f"\n{'='*50}")
    print(f"Comparing {name1} vs {name2}")
    print(f"{'='*50}")
    print(f"{name1}: {gc1:.2f}% GC")
    print(f"{name2}: {gc2:.2f}% GC")
    print(f"Difference: {abs(gc1 - gc2):.2f}%")
    
    if abs(gc1 - gc2) < 5:
        print("Similar GC content")
    elif gc1 > gc2:
        print(f"{name1} is more GC-rich")
    else:
        print(f"{name2} is more GC-rich")


if __name__ == "__main__":
    # Example 1: Analyze a single sequence
    print("EXAMPLE 1: GC Content Analysis")
    print("="*50)
    
    test_sequence = "ATGCGCGCGCTAGCGATCGATCGTAGCTAGCGATCGATCGTAGCTAGCGATCG"
    analyze_gc_content(test_sequence, window_size=10)
    
    # Example 2: Compare two sequences
    seq1 = "ATGCGCGCGCTAGCGATCG"  # GC-rich
    seq2 = "ATATATATAATATATATA"   # AT-rich
    
    compare_sequences(seq1, seq2, "GC-rich gene", "AT-rich gene")
    
    # Example 3: Human-like vs Bacteria-like
    print("\n" + "="*50)
    print("EXAMPLE 2: Human vs Bacterial GC Content")
    print("="*50)
    
    human_like = "ATGCTAGCTAGCATGCATGC" * 3  # ~50% GC
    bacterial_like = "GCGCGCGCGCGCGCGCGCGC" * 3  # ~100% GC
    
    compare_sequences(human_like, bacterial_like, "Human-like", "Bacterial-like")
