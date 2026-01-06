"""Tutorial 05: Loops - For loops, while loops, iteration"""
print("TUTORIAL 05: LOOPS AND ITERATION\n")

# For loop - iterate through list
genes = ['BRCA1', 'TP53', 'EGFR']
print("Looping through genes:")
for gene in genes:
    print(f"  Gene: {gene}")

# For loop - iterate through string
dna = "ATGC"
print("\nBases in DNA:")
for base in dna:
    print(f"  {base}")

# For loop with range
print("\nUsing range(5):")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# For loop with enumerate (get index + item)
sequences = ["ATGC", "GCTA", "CGAT"]
print("\nWith enumerate:")
for i, seq in enumerate(sequences):
    print(f"  Sequence {i}: {seq}")

# Splitting into codons
dna = "ATGCGCTAGGGCTAA"
print(f"\nSplitting {dna} into codons:")
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(f"  Position {i}: {codon}")

# Counting nucleotides
sequence = "ATGCGCTAGGGTAA"
print(f"\nCounting in {sequence}:")
for base in ['A', 'T', 'G', 'C']:
    count = sequence.count(base)
    print(f"  {base}: {count}")

# While loop
print("\nFinding ATG positions:")
dna = "AAATGCCATGGG"
position = 0
while position <= len(dna) - 3:
    if dna[position:position+3] == 'ATG':
        print(f"  Found ATG at position {position}")
    position += 1

# Nested loops
sequences = ["ATGC", "GCTA"]
bases = ['A', 'T', 'G', 'C']
print("\nNested loops - count each base in each sequence:")
for seq in sequences:
    print(f"  {seq}:")
    for base in bases:
        count = seq.count(base)
        print(f"    {base}: {count}")

# List comprehension (compact loop)
sequences = ["ATGC", "GCGC", "ATAT"]
lengths = [len(seq) for seq in sequences]
print(f"\nList comprehension:")
print(f"  Sequences: {sequences}")
print(f"  Lengths: {lengths}")

# Break and continue
print("\nBreak example - stop at first stop codon:")
sequence = "ATGCGCTAGGGGTAA"
for i in range(0, len(sequence)-2, 3):
    codon = sequence[i:i+3]
    print(f"  {codon}", end="")
    if codon in ['TAA', 'TAG', 'TGA']:
        print(" <- STOP")
        break
else:
    print()

print("\n✓ Key concepts: for loops, while loops, range(), enumerate(), break/continue")
