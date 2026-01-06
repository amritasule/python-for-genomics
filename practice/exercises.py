"""
PRACTICE EXERCISES
==================

Test your Python skills with genomics exercises!
Try to solve each one before checking solutions.py
"""

print("="*70)
print("PYTHON FOR GENOMICS - PRACTICE EXERCISES")
print("="*70)

# ============================================================================
# DATA STRUCTURES EXERCISES
# ============================================================================

print("\n" + "="*70)
print("DATA STRUCTURES EXERCISES")
print("="*70)

print("""
EXERCISE 1: Base Counter
-------------------------
Write a function that takes a DNA sequence and returns a dictionary
with the count of each base (A, T, G, C).

Example:
  count_bases("ATGCGC") → {'A': 1, 'T': 1, 'G': 2, 'C': 2}

Your code:
""")

def count_bases(sequence):
    # Your code here
    pass

# Test
test_seq = "ATGCGCTAGGGTAA"
print(f"Test: count_bases('{test_seq}')")
# Expected: {'A': 4, 'T': 3, 'G': 4, 'C': 3}

# ============================================================================

print("""
EXERCISE 2: Codon Extractor
----------------------------
Write a function that splits a DNA sequence into a list of codons (3-base groups).

Example:
  extract_codons("ATGCGCTAG") → ['ATG', 'CGC', 'TAG']

Your code:
""")

def extract_codons(sequence):
    # Your code here
    pass

# Test
test_seq = "ATGCGCTAGGGTAA"
print(f"Test: extract_codons('{test_seq}')")
# Expected: ['ATG', 'CGC', 'TAG', 'GGT']

# ============================================================================

print("""
EXERCISE 3: Reverse Complement
-------------------------------
Write a function that returns the reverse complement of a DNA sequence.

Example:
  reverse_complement("ATGC") → "GCAT"
  
Hint: Complement: A↔T, G↔C, then reverse the string

Your code:
""")

def reverse_complement(sequence):
    # Your code here
    pass

# Test
test_seq = "ATGCGC"
print(f"Test: reverse_complement('{test_seq}')")
# Expected: GCGCAT

# ============================================================================
# CONDITIONALS EXERCISES
# ============================================================================

print("\n" + "="*70)
print("CONDITIONALS EXERCISES")
print("="*70)

print("""
EXERCISE 4: Sequence Validator
-------------------------------
Write a function that checks if a sequence contains only valid DNA bases (A, T, G, C).
Return True if valid, False otherwise.

Example:
  is_valid_dna("ATGC") → True
  is_valid_dna("ATXC") → False

Your code:
""")

def is_valid_dna(sequence):
    # Your code here
    pass

# Test
print(f"Test: is_valid_dna('ATGC') → {is_valid_dna('ATGC')}")  # Expected: True
print(f"Test: is_valid_dna('ATXC') → {is_valid_dna('ATXC')}")  # Expected: False

# ============================================================================

print("""
EXERCISE 5: GC Classifier
--------------------------
Write a function that classifies a sequence by GC content:
  - "GC-rich" if GC > 60%
  - "Moderate" if 40% ≤ GC ≤ 60%
  - "AT-rich" if GC < 40%

Example:
  classify_gc("GCGCGC") → "GC-rich"

Your code:
""")

def classify_gc(sequence):
    # Your code here
    pass

# Test
print(f"Test: classify_gc('GCGCGC') → {classify_gc('GCGCGC')}")  # Expected: GC-rich

# ============================================================================

print("""
EXERCISE 6: ORF Checker
-----------------------
Write a function that checks if a sequence is a valid ORF:
  - Starts with ATG
  - Ends with a stop codon (TAA, TAG, or TGA)
  - Length is divisible by 3

Example:
  is_valid_orf("ATGCGCTAG") → True

Your code:
""")

def is_valid_orf(sequence):
    # Your code here
    pass

# Test
print(f"Test: is_valid_orf('ATGCGCTAG') → {is_valid_orf('ATGCGCTAG')}")  # Expected: True

# ============================================================================
# LOOPS EXERCISES
# ============================================================================

print("\n" + "="*70)
print("LOOPS EXERCISES")
print("="*70)

print("""
EXERCISE 7: Pattern Finder
---------------------------
Write a function that finds all positions of a motif in a sequence.
Return a list of positions (0-indexed).

Example:
  find_motif("ATGCATGATG", "ATG") → [0, 5, 8]

Your code:
""")

def find_motif(sequence, motif):
    # Your code here
    pass

# Test
test_seq = "ATGCATGATG"
test_motif = "ATG"
print(f"Test: find_motif('{test_seq}', '{test_motif}')")
# Expected: [0, 5, 8]

# ============================================================================

print("""
EXERCISE 8: Sequence Comparer
------------------------------
Write a function that compares two sequences of the same length
and returns the percentage of matching bases.

Example:
  calculate_similarity("ATGC", "ATCC") → 75.0

Your code:
""")

def calculate_similarity(seq1, seq2):
    # Your code here
    pass

# Test
print(f"Test: calculate_similarity('ATGC', 'ATCC')")
# Expected: 75.0

# ============================================================================

print("""
EXERCISE 9: Multiple Frame ORF Finder
--------------------------------------
Write a function that finds all ORFs in all three reading frames.
Return a list of tuples: (frame, start_pos, orf_sequence)

Example:
  find_orfs_all_frames("ATGCGCTAGATGGGGTAA")
  → [(0, 0, 'ATGCGCTAG'), (0, 9, 'ATGGGGTAA')]

Your code:
""")

def find_orfs_all_frames(sequence):
    # Your code here
    pass

# Test
test_seq = "ATGCGCTAGATGGGGTAA"
print(f"Test: find_orfs_all_frames('{test_seq}')")

# ============================================================================
# FILE I/O EXERCISES
# ============================================================================

print("\n" + "="*70)
print("FILE I/O EXERCISES")
print("="*70)

print("""
EXERCISE 10: FASTA Reader
--------------------------
Write a function that reads a FASTA file and returns a dictionary
with headers as keys and sequences as values.

FASTA format:
>header
SEQUENCE

Your code:
""")

def read_fasta(filename):
    # Your code here
    pass

# Test
print("Test: read_fasta('../data/sample_sequences.fasta')")

# ============================================================================

print("""
EXERCISE 11: Sequence Filter
-----------------------------
Write a function that:
1. Reads sequences from a FASTA file
2. Filters sequences by minimum length
3. Writes filtered sequences to a new FASTA file

Your code:
""")

def filter_by_length(input_file, output_file, min_length):
    # Your code here
    pass

# Test
print("Test: filter_by_length('input.fasta', 'output.fasta', 20)")

# ============================================================================

print("""
EXERCISE 12: FASTA Merger
--------------------------
Write a function that merges multiple FASTA files into one.

Your code:
""")

def merge_fasta_files(input_files, output_file):
    # Your code here
    pass

# Test
print("Test: merge_fasta_files(['file1.fasta', 'file2.fasta'], 'merged.fasta')")

# ============================================================================

print("\n" + "="*70)
print("DONE! Check solutions.py for answers")
print("="*70)
