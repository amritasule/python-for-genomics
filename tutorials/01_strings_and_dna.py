"""
Tutorial 01: Strings and DNA Sequences

Learn: String basics, indexing, slicing, methods
Genomics: Working with DNA sequences
"""

print("=" * 70)
print("TUTORIAL 01: STRINGS AND DNA SEQUENCES")
print("=" * 70)

# =============================================================================
# SECTION 1: CREATING STRINGS
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 1: Creating Strings")
print("─" * 70)

# Strings are text in quotes
dna_sequence = "ATGCGCTA"
gene_name = 'BRCA1'
description = """This is a multi-line string
for longer descriptions"""

print(f"DNA sequence: {dna_sequence}")
print(f"Gene name: {gene_name}")
print(f"Type: {type(dna_sequence)}")  # <class 'str'>

# =============================================================================
# SECTION 2: STRING LENGTH
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 2: String Length")
print("─" * 70)

sequence = "ATGCGCTAGGGTAA"
length = len(sequence)

print(f"Sequence: {sequence}")
print(f"Length: {length} bp (base pairs)")

# =============================================================================
# SECTION 3: INDEXING - Accessing Individual Characters
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 3: Indexing (Accessing Single Bases)")
print("─" * 70)

#      Positions: 0 1 2 3 4 5 6 7
sequence = "ATGCGCTA"
#     Negative: -8-7-6-5-4-3-2-1

print(f"Sequence: {sequence}")
print(f"\nPositive indexing:")
print(f"  First base (position 0): {sequence[0]}")
print(f"  Second base (position 1): {sequence[1]}")
print(f"  Fourth base (position 3): {sequence[3]}")

print(f"\nNegative indexing:")
print(f"  Last base (position -1): {sequence[-1]}")
print(f"  Second to last (position -2): {sequence[-2]}")

# Common use: Check start codon
print(f"\nStart codon check:")
print(f"  Position 0-2: {sequence[0]}{sequence[1]}{sequence[2]}")

# =============================================================================
# SECTION 4: SLICING - Getting Substrings
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 4: Slicing (Getting Subsequences)")
print("─" * 70)

sequence = "ATGCGCTAGGGTAA"

print(f"Sequence: {sequence}")
print(f"\nBasic slicing [start:end]:")
print(f"  sequence[0:3] = {sequence[0:3]}  (first 3 bases)")
print(f"  sequence[3:6] = {sequence[3:6]}  (bases 3-5)")
print(f"  sequence[6:9] = {sequence[6:9]}  (bases 6-8)")

print(f"\nOmitting start/end:")
print(f"  sequence[:3] = {sequence[:3]}    (first 3)")
print(f"  sequence[3:] = {sequence[3:]}    (from position 3 to end)")
print(f"  sequence[:] = {sequence[:]}      (entire sequence)")

print(f"\nNegative indices:")
print(f"  sequence[-3:] = {sequence[-3:]}  (last 3 bases)")
print(f"  sequence[:-3] = {sequence[:-3]}  (all except last 3)")

print(f"\nStep parameter [start:end:step]:")
print(f"  sequence[::2] = {sequence[::2]}   (every 2nd base)")
print(f"  sequence[::3] = {sequence[::3]}   (every 3rd base)")
print(f"  sequence[::-1] = {sequence[::-1]} (reverse!)")

# Genomics application: Split into codons
print(f"\nSplit into codons:")
codon1 = sequence[0:3]
codon2 = sequence[3:6]
codon3 = sequence[6:9]
print(f"  Codon 1: {codon1}")
print(f"  Codon 2: {codon2}")
print(f"  Codon 3: {codon3}")

# =============================================================================
# SECTION 5: STRING METHODS
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 5: String Methods")
print("─" * 70)

sequence = "ATGCGCTagggtaa"

# Case conversion
print(f"Original: {sequence}")
print(f"Upper: {sequence.upper()}")
print(f"Lower: {sequence.lower()}")

# Counting
clean_seq = sequence.upper()
print(f"\nCounting bases:")
print(f"  A's: {clean_seq.count('A')}")
print(f"  T's: {clean_seq.count('T')}")
print(f"  G's: {clean_seq.count('G')}")
print(f"  C's: {clean_seq.count('C')}")
print(f"  ATG codons: {clean_seq.count('ATG')}")

# Finding positions
print(f"\nFinding positions:")
print(f"  First 'ATG' at position: {clean_seq.find('ATG')}")
print(f"  First 'TAA' at position: {clean_seq.find('TAA')}")
print(f"  'XYZ' (not found): {clean_seq.find('XYZ')}")  # Returns -1

# Checking contents
print(f"\nChecking contents:")
print(f"  Starts with 'ATG': {clean_seq.startswith('ATG')}")
print(f"  Ends with 'TAA': {clean_seq.endswith('TAA')}")
print(f"  Contains 'GGG': {'GGG' in clean_seq}")

# Replacing
mutated = clean_seq.replace('A', 'T')
print(f"\nReplacement:")
print(f"  Original: {clean_seq}")
print(f"  All A→T: {mutated}")

# Splitting
fasta_header = ">gene1|BRCA1|human"
parts = fasta_header.split('|')
print(f"\nSplitting:")
print(f"  Original: {fasta_header}")
print(f"  Split by '|': {parts}")

# =============================================================================
# SECTION 6: STRING CONCATENATION
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 6: Combining Strings")
print("─" * 70)

# Using +
part1 = "ATG"
part2 = "CGC"
part3 = "TAG"
combined = part1 + part2 + part3
print(f"Combining with +: {combined}")

# Using join (more efficient)
parts = ["ATG", "CGC", "TAG"]
combined2 = "".join(parts)
print(f"Combining with join: {combined2}")

# Repeating
repeat_unit = "CAG"
repeated = repeat_unit * 10
print(f"\nRepeating 'CAG' 10 times: {repeated}")

# =============================================================================
# SECTION 7: STRING FORMATTING
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 7: String Formatting")
print("─" * 70)

gene = "BRCA1"
length = 100
gc_content = 65.432

# f-strings (modern, recommended)
print(f"Gene: {gene}, Length: {length}bp, GC: {gc_content:.2f}%")

# Formatting numbers
print(f"\nFormatting examples:")
print(f"  2 decimals: {gc_content:.2f}%")
print(f"  1 decimal: {gc_content:.1f}%")
print(f"  No decimals: {gc_content:.0f}%")
print(f"  With commas: {1234567:,} bases")

# =============================================================================
# SECTION 8: PRACTICAL GENOMICS EXAMPLES
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 8: Practical Genomics Examples")
print("─" * 70)

# Example 1: Calculate GC content
sequence = "ATGCGCTAGGGTAA"
g_count = sequence.count('G')
c_count = sequence.count('C')
total = len(sequence)
gc_percent = ((g_count + c_count) / total) * 100

print(f"\nExample 1: GC Content")
print(f"  Sequence: {sequence}")
print(f"  G count: {g_count}")
print(f"  C count: {c_count}")
print(f"  GC%: {gc_percent:.1f}%")

# Example 2: Get complement
sequence = "ATGC"
complement = ""
for base in sequence:
    if base == 'A':
        complement += 'T'
    elif base == 'T':
        complement += 'A'
    elif base == 'G':
        complement += 'C'
    elif base == 'C':
        complement += 'G'

print(f"\nExample 2: Complement")
print(f"  Original: {sequence}")
print(f"  Complement: {complement}")

# Example 3: Extract all codons
sequence = "ATGCGCTAGGGTAA"
print(f"\nExample 3: Extract Codons")
print(f"  Sequence: {sequence}")
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    print(f"  Position {i}: {codon}")

# Example 4: Validate DNA
def is_valid_dna(seq):
    """Check if sequence contains only A, T, G, C"""
    seq = seq.upper()
    for base in seq:
        if base not in 'ATGC':
            return False
    return True

print(f"\nExample 4: Validate DNA")
test1 = "ATGC"
test2 = "ATXC"
print(f"  '{test1}' valid: {is_valid_dna(test1)}")
print(f"  '{test2}' valid: {is_valid_dna(test2)}")

# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
Try these exercises:

1. Create a DNA sequence and print its length
2. Extract the first codon (first 3 bases)
3. Reverse a DNA sequence using slicing
4. Count how many 'A' bases are in "ATGCGCTAGGGTAA"
5. Check if a sequence starts with "ATG"
6. Replace all 'A' with 'T' in a sequence
7. Split this into codons: "ATGCGCTAGGGCTAA"
8. Calculate AT content (percentage of A and T)

Hint: Try writing the code in Python interpreter!
""")

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)

print("""
✓ Strings store text (like DNA sequences)
✓ Index with [0], [-1] for first/last character
✓ Slice with [start:end] to get subsequences
✓ Use methods: .upper(), .count(), .find(), .replace()
✓ Check contents with 'in' and .startswith()
✓ Format with f-strings: f"GC: {gc:.2f}%"
✓ DNA sequences are just strings in Python!
""")

print("\nNext: Tutorial 02 - Lists and Sequences")
