"""
Tutorial 02: Lists and Sequences

Learn: Lists, indexing, methods, comprehensions
Genomics: Working with multiple sequences, codons
"""

print("=" * 70)
print("TUTORIAL 02: LISTS AND SEQUENCES")
print("=" * 70)

# =============================================================================
# SECTION 1: CREATING LISTS
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 1: Creating Lists")
print("─" * 70)

# Lists hold multiple items
genes = ["BRCA1", "TP53", "EGFR", "MYC"]
bases = ['A', 'T', 'G', 'C']
counts = [10, 20, 15, 30]
mixed = ["BRCA1", 100, True, 3.14]  # Can mix types

print(f"Genes: {genes}")
print(f"Bases: {bases}")
print(f"Counts: {counts}")
print(f"Mixed types: {mixed}")
print(f"Type: {type(genes)}")  # <class 'list'>

# Empty list
empty = []
sequences = list()  # Another way

print(f"Empty list: {empty}")

# =============================================================================
# SECTION 2: ACCESSING LIST ELEMENTS (INDEXING)
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 2: Accessing List Elements")
print("─" * 70)

#    Index: 0        1      2       3
genes = ["BRCA1", "TP53", "EGFR", "MYC"]
# Negative: -4      -3     -2      -1

print(f"Genes: {genes}")
print(f"\nPositive indexing:")
print(f"  First gene [0]: {genes[0]}")
print(f"  Second gene [1]: {genes[1]}")

print(f"\nNegative indexing:")
print(f"  Last gene [-1]: {genes[-1]}")
print(f"  Second to last [-2]: {genes[-2]}")

# =============================================================================
# SECTION 3: LIST SLICING
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 3: List Slicing")
print("─" * 70)

sequences = ["ATGC", "GCTA", "CGAT", "TAGC", "ATAT"]

print(f"Sequences: {sequences}")
print(f"\nSlicing:")
print(f"  First 3 [0:3]: {sequences[0:3]}")
print(f"  Last 2 [-2:]: {sequences[-2:]}")
print(f"  Middle [1:4]: {sequences[1:4]}")
print(f"  Every 2nd [::2]: {sequences[::2]}")
print(f"  Reversed [::-1]: {sequences[::-1]}")

# =============================================================================
# SECTION 4: LIST LENGTH
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 4: List Length")
print("─" * 70)

genes = ["BRCA1", "TP53", "EGFR"]
print(f"Genes: {genes}")
print(f"Number of genes: {len(genes)}")

# =============================================================================
# SECTION 5: MODIFYING LISTS (Lists are Mutable!)
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 5: Modifying Lists")
print("─" * 70)

genes = ["BRCA1", "TP53", "EGFR"]
print(f"Original: {genes}")

# Change an element
genes[1] = "KRAS"
print(f"After changing [1]: {genes}")

# Add to end
genes.append("MYC")
print(f"After append: {genes}")

# Insert at position
genes.insert(0, "APC")
print(f"After insert at [0]: {genes}")

# Remove by value
genes.remove("EGFR")
print(f"After remove 'EGFR': {genes}")

# Remove by position
popped = genes.pop()  # Removes and returns last
print(f"Popped: {popped}")
print(f"After pop: {genes}")

# Remove specific position
del genes[1]
print(f"After del [1]: {genes}")

# =============================================================================
# SECTION 6: LIST METHODS
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 6: List Methods")
print("─" * 70)

# Sorting
numbers = [15, 3, 42, 8, 1]
print(f"Original: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")

genes = ["BRCA1", "TP53", "EGFR", "APC"]
genes.sort()
print(f"Sorted genes: {genes}")

# Reversing
genes.reverse()
print(f"After reverse(): {genes}")

# Counting
sequences = ["ATGC", "GCTA", "ATGC", "ATGC", "CGAT"]
count = sequences.count("ATGC")
print(f"\nSequences: {sequences}")
print(f"'ATGC' appears {count} times")

# Finding index
position = sequences.index("CGAT")
print(f"'CGAT' is at position: {position}")

# Extending (combine lists)
list1 = ["A", "T"]
list2 = ["G", "C"]
list1.extend(list2)
print(f"\nAfter extend: {list1}")

# Clearing
test = [1, 2, 3]
test.clear()
print(f"After clear: {test}")

# =============================================================================
# SECTION 7: LIST OPERATIONS
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 7: List Operations")
print("─" * 70)

# Concatenation with +
list1 = ["ATG", "CGC"]
list2 = ["TAG", "GGG"]
combined = list1 + list2
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Combined: {combined}")

# Repetition with *
repeat = ["CAG"] * 5
print(f"\n['CAG'] * 5 = {repeat}")

# Membership testing
genes = ["BRCA1", "TP53", "EGFR"]
print(f"\nGenes: {genes}")
print(f"'BRCA1' in list: {'BRCA1' in genes}")
print(f"'MYC' in list: {'MYC' in genes}")

# Min, Max, Sum (for numbers)
gc_values = [45.2, 52.1, 38.9, 67.3]
print(f"\nGC values: {gc_values}")
print(f"Minimum: {min(gc_values)}")
print(f"Maximum: {max(gc_values)}")
print(f"Average: {sum(gc_values) / len(gc_values):.1f}")

# =============================================================================
# SECTION 8: SPLITTING STRINGS INTO LISTS
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 8: Converting Strings to Lists")
print("─" * 70)

# Split DNA into codons
dna = "ATGCGCTAGGGCTAA"
print(f"DNA: {dna}")

# Method 1: Loop with slicing
codons = []
for i in range(0, len(dna), 3):
    codons.append(dna[i:i+3])
print(f"Codons (loop): {codons}")

# Method 2: List comprehension (we'll learn this soon!)
codons2 = [dna[i:i+3] for i in range(0, len(dna), 3)]
print(f"Codons (comprehension): {codons2}")

# Split by delimiter
fasta_header = "gene1|BRCA1|human|chr17"
parts = fasta_header.split('|')
print(f"\nHeader: {fasta_header}")
print(f"Split: {parts}")

# Split into individual characters
sequence = "ATGC"
bases = list(sequence)
print(f"\nSequence: {sequence}")
print(f"As list: {bases}")

# =============================================================================
# SECTION 9: JOINING LISTS INTO STRINGS
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 9: Converting Lists to Strings")
print("─" * 70)

codons = ["ATG", "CGC", "TAG"]
print(f"Codons: {codons}")

# Join with no separator
sequence = "".join(codons)
print(f"Joined (no separator): {sequence}")

# Join with separator
formatted = "-".join(codons)
print(f"Joined (with '-'): {formatted}")

# Join with space
genes = ["BRCA1", "TP53", "EGFR"]
gene_list = ", ".join(genes)
print(f"\nGenes: {gene_list}")

# =============================================================================
# SECTION 10: NESTED LISTS (Lists of Lists)
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 10: Nested Lists")
print("─" * 70)

# Each experiment has multiple replicates
experiment_data = [
    ["ATGC", "GCTA", "CGAT"],  # Day 1
    ["TAGC", "ATAT", "GCGC"],  # Day 2
    ["CCGG", "TTAA", "GGCC"]   # Day 3
]

print(f"All data: {experiment_data}")
print(f"Day 1 data: {experiment_data[0]}")
print(f"Day 2, Replicate 2: {experiment_data[1][1]}")

# =============================================================================
# SECTION 11: LIST COMPREHENSIONS (Advanced but Powerful!)
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 11: List Comprehensions")
print("─" * 70)

# Instead of this:
numbers = []
for i in range(5):
    numbers.append(i * 2)
print(f"Traditional loop: {numbers}")

# Use this (more Pythonic):
numbers2 = [i * 2 for i in range(5)]
print(f"List comprehension: {numbers2}")

# Genomics examples
sequences = ["ATGC", "GCTA", "CGAT", "TAGC"]

# Get lengths
lengths = [len(seq) for seq in sequences]
print(f"\nSequences: {sequences}")
print(f"Lengths: {lengths}")

# Convert to uppercase
upper_seqs = [seq.upper() for seq in sequences]
print(f"Uppercase: {upper_seqs}")

# With condition (filter)
long_seqs = [seq for seq in sequences if len(seq) >= 4]
print(f"4+ bases: {long_seqs}")

# Calculate GC content for each
gc_contents = [((s.count('G') + s.count('C')) / len(s)) * 100 
               for s in sequences]
print(f"GC contents: {[f'{gc:.1f}%' for gc in gc_contents]}")

# =============================================================================
# SECTION 12: PRACTICAL GENOMICS EXAMPLES
# =============================================================================

print("\n" + "─" * 70)
print("SECTION 12: Practical Genomics Examples")
print("─" * 70)

# Example 1: Process multiple sequences
print("\nExample 1: Analyze Multiple Sequences")
sequences = ["ATGCGC", "GCTAGC", "TATAAA"]

for i, seq in enumerate(sequences, 1):
    length = len(seq)
    gc = ((seq.count('G') + seq.count('C')) / length) * 100
    print(f"  Seq {i}: {seq} ({length}bp, GC={gc:.1f}%)")

# Example 2: Collect sequences with specific feature
print("\nExample 2: Filter Sequences with Start Codon")
sequences = ["ATGCGC", "GCTAGC", "ATGAAA", "TATAAA"]
with_start = []

for seq in sequences:
    if seq.startswith("ATG"):
        with_start.append(seq)

print(f"  Original: {sequences}")
print(f"  With ATG: {with_start}")

# Example 3: Find best sequence (highest GC)
print("\nExample 3: Find Highest GC Content")
sequences = ["ATGCGC", "GCGCGC", "ATATAT"]
gc_values = []

for seq in sequences:
    gc = ((seq.count('G') + seq.count('C')) / len(seq)) * 100
    gc_values.append(gc)

max_gc = max(gc_values)
best_index = gc_values.index(max_gc)
best_seq = sequences[best_index]

print(f"  Sequences: {sequences}")
print(f"  GC values: {[f'{gc:.1f}%' for gc in gc_values]}")
print(f"  Highest GC: {best_seq} ({max_gc:.1f}%)")

# Example 4: Batch process - get all codons from multiple sequences
print("\nExample 4: Extract Codons from Multiple Sequences")
sequences = ["ATGCGCTAG", "GCTAGCGAT"]

all_codons = []
for seq in sequences:
    seq_codons = [seq[i:i+3] for i in range(0, len(seq), 3)]
    all_codons.extend(seq_codons)

print(f"  Sequences: {sequences}")
print(f"  All codons: {all_codons}")
print(f"  Unique codons: {list(set(all_codons))}")

# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
Try these exercises:

1. Create a list of 5 DNA sequences
2. Add a new sequence to the end
3. Remove the third sequence
4. Print the first and last sequences
5. Sort the list alphabetically
6. Count how many times "ATGC" appears in the list
7. Split "ATGCGCTAGGGTAA" into a list of codons
8. Join the list ["ATG", "CGC", "TAG"] into one sequence
9. Create a list of all GC contents for ["ATGC", "GCGC", "ATAT"]
10. Filter to keep only sequences starting with "ATG"

Hint: Practice in Python interpreter!
""")

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)

print("""
✓ Lists store multiple items: genes = ["BRCA1", "TP53"]
✓ Access with index: genes[0]
✓ Slice like strings: genes[0:2]
✓ Lists are MUTABLE (can change)
✓ Common methods: .append(), .remove(), .sort()
✓ Split strings to lists: dna.split() or list(dna)
✓ Join lists to strings: "".join(codons)
✓ List comprehensions: [x*2 for x in numbers]
✓ Perfect for multiple sequences!
""")

print("\nNext: Tutorial 03 - Dictionaries and Codons")
