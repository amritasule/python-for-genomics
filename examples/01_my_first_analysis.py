"""
My First DNA Analysis - Super Simple Example
Perfect for beginners learning Python and genomics!
"""

import sys
sys.path.append('../modules')
import dna_tools

print("="*50)
print("MY FIRST DNA ANALYSIS")
print("="*50)

# Step 1: Define a DNA sequence
my_sequence = "ATGCGCTAGGGTAA"
print(f"\nStep 1: My DNA sequence")
print(f"Sequence: {my_sequence}")
print(f"Length: {len(my_sequence)} bp")

# Step 2: Count the bases
print(f"\nStep 2: Count each base")
counts = dna_tools.count_nucleotides(my_sequence)
print(f"A (Adenine):  {counts['A']}")
print(f"T (Thymine):  {counts['T']}")
print(f"G (Guanine):  {counts['G']}")
print(f"C (Cytosine): {counts['C']}")

# Step 3: Calculate GC content
print(f"\nStep 3: Calculate GC content")
gc = dna_tools.gc_content(my_sequence)
print(f"GC Content: {gc:.2f}%")
if gc > 50:
    print("This is a GC-rich sequence!")
else:
    print("This is an AT-rich sequence!")

# Step 4: Get the complement
print(f"\nStep 4: Find the complement")
comp = dna_tools.complement(my_sequence)
print(f"Original:   {my_sequence}")
print(f"Complement: {comp}")

# Step 5: Get reverse complement
print(f"\nStep 5: Find the reverse complement")
rev_comp = dna_tools.reverse_complement(my_sequence)
print(f"Original:          {my_sequence}")
print(f"Reverse Complement: {rev_comp}")

# Step 6: Transcribe to RNA
print(f"\nStep 6: Transcribe DNA to RNA")
rna = dna_tools.transcribe(my_sequence)
print(f"DNA: {my_sequence}")
print(f"RNA: {rna}")

# Step 7: Translate to protein
print(f"\nStep 7: Translate to protein")
protein = dna_tools.translate(my_sequence)
print(f"DNA:     {my_sequence}")
print(f"Protein: {protein}")
print(f"  (M = Methionine, R = Arginine, * = Stop codon, G = Glycine)")

# Step 8: Check for special codons
print(f"\nStep 8: Look for special codons")
has_start = dna_tools.has_start_codon(my_sequence)
has_stop = dna_tools.has_stop_codon(my_sequence)
print(f"Has START codon (ATG): {has_start}")
print(f"Has STOP codon: {has_stop}")

print("\n" + "="*50)
print("Analysis complete! 🧬")
print("="*50)
