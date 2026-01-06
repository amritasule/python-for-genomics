"""
Compare Two DNA Sequences
Learn how sequences can be similar or different!
"""

import sys
sys.path.append('../modules')
import dna_tools
import sequence_analysis

def compare_sequences(seq1, seq2, name1="Sequence 1", name2="Sequence 2"):
    """Compare two DNA sequences side by side."""
    
    print("\n" + "="*60)
    print(f"COMPARING: {name1} vs {name2}")
    print("="*60)
    
    # Display sequences
    print(f"\n{name1}:")
    print(f"  {seq1}")
    print(f"\n{name2}:")
    print(f"  {seq2}")
    
    # Length comparison
    print(f"\n📏 LENGTH:")
    print(f"  {name1}: {len(seq1)} bp")
    print(f"  {name2}: {len(seq2)} bp")
    if len(seq1) == len(seq2):
        print(f"  → Same length!")
    else:
        print(f"  → Different lengths (Δ = {abs(len(seq1) - len(seq2))} bp)")
    
    # GC content comparison
    print(f"\n📊 GC CONTENT:")
    gc1 = dna_tools.gc_content(seq1)
    gc2 = dna_tools.gc_content(seq2)
    print(f"  {name1}: {gc1:.2f}%")
    print(f"  {name2}: {gc2:.2f}%")
    print(f"  → Difference: {abs(gc1-gc2):.2f}%")
    
    # Hamming distance (if same length)
    if len(seq1) == len(seq2):
        print(f"\n🔍 SIMILARITY:")
        hamming = sequence_analysis.hamming_distance(seq1, seq2)
        similarity = (1 - hamming/len(seq1)) * 100
        print(f"  Differences: {hamming} positions")
        print(f"  Similarity: {similarity:.1f}%")
        
        # Show differences
        if hamming > 0 and hamming <= 10:
            print(f"\n  Positions that differ:")
            for i, (base1, base2) in enumerate(zip(seq1, seq2)):
                if base1 != base2:
                    print(f"    Position {i}: {base1} → {base2}")
    else:
        print(f"\n🔍 SIMILARITY:")
        print(f"  Can't calculate (different lengths)")
    
    # Translation comparison (if both are multiples of 3)
    if len(seq1) % 3 == 0 and len(seq2) % 3 == 0:
        print(f"\n🧫 PROTEINS:")
        protein1 = dna_tools.translate(seq1)
        protein2 = dna_tools.translate(seq2)
        print(f"  {name1}: {protein1}")
        print(f"  {name2}: {protein2}")
        if protein1 == protein2:
            print(f"  → Same protein!")
        else:
            print(f"  → Different proteins")
    
    print("\n" + "="*60)


# Example 1: Very similar sequences (single mutation)
print("\n🧬 EXAMPLE 1: Single Mutation")
print("What happens when just ONE base changes?")

seq1 = "ATGCGCTAGGGTAA"
seq2 = "ATGCGCTAGGATAA"  # One G changed to A
#                    ^

compare_sequences(seq1, seq2, "Original", "Mutated")

# Example 2: GC-rich vs AT-rich
print("\n\n🧬 EXAMPLE 2: GC-rich vs AT-rich")
print("How different are GC-rich and AT-rich sequences?")

gc_rich = "GCGCGCGCGCGCGC"
at_rich = "ATATATATAT ATATAT"

compare_sequences(gc_rich, at_rich, "GC-rich", "AT-rich")

# Example 3: Complement sequences
print("\n\n🧬 EXAMPLE 3: Complementary Sequences")
print("How do complementary DNA strands compare?")

original = "ATGCGCTA"
complement = dna_tools.complement(original)

compare_sequences(original, complement, "Original", "Complement")

print("\n✨ Done! Try modifying the sequences in this script to compare your own!")
