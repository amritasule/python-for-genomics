"""
Basic DNA Operations - The Simplest Example
Learn what each function does, one at a time!
"""

import sys
sys.path.append('../modules')
import dna_tools

# Our example DNA sequence
dna = "ATGCGCTAGGGTAA"

print("🧬 BASIC DNA OPERATIONS")
print("="*50)
print(f"\nOur DNA sequence: {dna}")
print(f"Length: {len(dna)} base pairs")
print("\n" + "="*50)

# 1. Validate DNA
print("\n1️⃣  VALIDATE DNA")
print("   Check if sequence contains only A, T, G, C")
is_valid = dna_tools.validate_dna(dna)
print(f"   Result: {is_valid}")
print(f"   ✓ This is valid DNA!")

# 2. Count nucleotides
print("\n2️⃣  COUNT NUCLEOTIDES")
print("   Count how many of each base")
counts = dna_tools.count_nucleotides(dna)
print(f"   A: {counts['A']}")
print(f"   T: {counts['T']}")
print(f"   G: {counts['G']}")
print(f"   C: {counts['C']}")

# 3. GC Content
print("\n3️⃣  GC CONTENT")
print("   Percentage of G and C bases")
gc = dna_tools.gc_content(dna)
print(f"   GC Content: {gc:.2f}%")

# 4. AT Content
print("\n4️⃣  AT CONTENT")
print("   Percentage of A and T bases")
at = dna_tools.at_content(dna)
print(f"   AT Content: {at:.2f}%")

# 5. Complement
print("\n5️⃣  COMPLEMENT")
print("   A↔T and G↔C")
print(f"   Original:   {dna}")
comp = dna_tools.complement(dna)
print(f"   Complement: {comp}")

# 6. Reverse Complement
print("\n6️⃣  REVERSE COMPLEMENT")
print("   Complement + Reverse (3' to 5')")
print(f"   Original:          {dna}")
rev_comp = dna_tools.reverse_complement(dna)
print(f"   Reverse Complement: {rev_comp}")

# 7. Transcribe (DNA → RNA)
print("\n7️⃣  TRANSCRIBE (DNA → RNA)")
print("   Replace T with U")
print(f"   DNA: {dna}")
rna = dna_tools.transcribe(dna)
print(f"   RNA: {rna}")

# 8. Translate (DNA → Protein)
print("\n8️⃣  TRANSLATE (DNA → Protein)")
print("   Convert codons to amino acids")
print(f"   DNA:     {dna}")
protein = dna_tools.translate(dna)
print(f"   Protein: {protein}")
print(f"   (Each letter = one amino acid)")

# 9. Check for Start Codon
print("\n9️⃣  CHECK FOR START CODON (ATG)")
has_start = dna_tools.has_start_codon(dna)
print(f"   Has ATG: {has_start}")
if has_start:
    position = dna.find("ATG")
    print(f"   ✓ Found at position {position}")

# 10. Check for Stop Codon
print("\n🔟 CHECK FOR STOP CODON (TAA, TAG, TGA)")
has_stop = dna_tools.has_stop_codon(dna)
print(f"   Has stop codon: {has_stop}")
if has_stop:
    for stop in ['TAA', 'TAG', 'TGA']:
        if stop in dna:
            position = dna.find(stop)
            print(f"   ✓ Found {stop} at position {position}")

print("\n" + "="*50)
print("✨ That's it! These are the basic operations.")
print("="*50)

# Try with your own sequence!
print("\n💡 TIP: Change the 'dna' variable at the top")
print("   to analyze your own sequence!")
