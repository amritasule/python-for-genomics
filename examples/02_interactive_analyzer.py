"""
Interactive DNA Analyzer
Type in your own DNA sequence and analyze it!
"""

import sys
sys.path.append('../modules')
import dna_tools

def analyze_my_sequence(sequence):
    """Analyze a DNA sequence and print results."""
    
    # Validate the sequence
    if not dna_tools.validate_dna(sequence):
        print("❌ ERROR: This is not a valid DNA sequence!")
        print("DNA sequences can only contain A, T, G, and C")
        return
    
    print("\n" + "="*60)
    print(f"ANALYZING: {sequence}")
    print("="*60)
    
    # Basic info
    print(f"\n📊 BASIC INFO:")
    print(f"  Length: {len(sequence)} base pairs")
    print(f"  Valid DNA: ✓")
    
    # Composition
    print(f"\n🧪 COMPOSITION:")
    counts = dna_tools.count_nucleotides(sequence)
    total = len(sequence)
    print(f"  A: {counts['A']} ({counts['A']/total*100:.1f}%)")
    print(f"  T: {counts['T']} ({counts['T']/total*100:.1f}%)")
    print(f"  G: {counts['G']} ({counts['G']/total*100:.1f}%)")
    print(f"  C: {counts['C']} ({counts['C']/total*100:.1f}%)")
    
    # GC content
    gc = dna_tools.gc_content(sequence)
    print(f"\n📈 GC CONTENT: {gc:.2f}%")
    if gc > 60:
        print("  → Very GC-rich (like bacteria)")
    elif gc > 40:
        print("  → Moderate GC (like humans)")
    else:
        print("  → AT-rich")
    
    # Reverse complement
    print(f"\n🔄 REVERSE COMPLEMENT:")
    print(f"  {dna_tools.reverse_complement(sequence)}")
    
    # RNA
    print(f"\n🧬 RNA:")
    print(f"  {dna_tools.transcribe(sequence)}")
    
    # Protein (if multiple of 3)
    if len(sequence) % 3 == 0:
        print(f"\n🧫 PROTEIN:")
        protein = dna_tools.translate(sequence)
        print(f"  {protein}")
    else:
        print(f"\n🧫 PROTEIN:")
        print(f"  ⚠️  Length not divisible by 3 (need complete codons)")
    
    # Special features
    print(f"\n⭐ SPECIAL FEATURES:")
    if dna_tools.has_start_codon(sequence):
        print(f"  ✓ Has START codon (ATG)")
    if dna_tools.has_stop_codon(sequence):
        print(f"  ✓ Has STOP codon")
    
    print("\n" + "="*60)


# Main program
print("🧬 INTERACTIVE DNA ANALYZER 🧬")
print("="*60)
print("\nTry these examples or enter your own:")
print("  1. ATGCGCTAGGGTAA")
print("  2. GCGCGCGCGC")
print("  3. ATATATAT")
print("  4. Your own sequence!")

# Example sequences
examples = {
    "1": "ATGCGCTAGGGTAA",
    "2": "GCGCGCGCGC",
    "3": "ATATATAT"
}

print("\nType a number (1-3) or enter your own DNA sequence:")
user_input = input("> ").strip()

# Check if it's an example number or custom sequence
if user_input in examples:
    sequence = examples[user_input]
    print(f"\nUsing example {user_input}")
else:
    sequence = user_input.upper()

# Analyze it
analyze_my_sequence(sequence)

print("\n✨ Done! Run this script again to analyze another sequence.")
