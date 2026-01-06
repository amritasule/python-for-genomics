"""Tutorial 04: Conditionals - If statements, comparisons, validation"""
print("TUTORIAL 04: CONDITIONALS IN GENOMICS\n")

# If statements
sequence = "ATGCGCTA"
if 'ATG' in sequence:
    print(f"✓ {sequence} has start codon")

# If-else
if len(sequence) > 10:
    print("Long sequence")
else:
    print("Short sequence")

# If-elif-else
gc = 65.0
if gc > 60:
    print(f"GC-rich: {gc}%")
elif gc > 40:
    print(f"Moderate: {gc}%")
else:
    print(f"AT-rich: {gc}%")

# Comparisons: ==, !=, <, >, <=, >=
print(f"\nlen(sequence) > 5: {len(sequence) > 5}")
print(f"sequence == 'ATGC': {sequence == 'ATGC'}")

# Logical operators: and, or, not
has_start = 'ATG' in sequence
has_stop = 'TAA' in sequence
print(f"\nhas_start AND has_stop: {has_start and has_stop}")
print(f"has_start OR has_stop: {has_start or has_stop}")
print(f"NOT has_start: {not has_start}")

# Validation example
def is_valid_dna(seq):
    if len(seq) == 0:
        return False
    for base in seq.upper():
        if base not in 'ATGC':
            return False
    return True

print(f"\nis_valid_dna('ATGC'): {is_valid_dna('ATGC')}")
print(f"is_valid_dna('ATXC'): {is_valid_dna('ATXC')}")

# Classification example
def classify_gc(seq):
    gc = ((seq.count('G') + seq.count('C')) / len(seq)) * 100
    if gc < 40:
        return "AT-rich"
    elif gc < 60:
        return "Moderate"
    else:
        return "GC-rich"

test_seqs = ["ATATATAT", "ATGCGCTA", "GCGCGCGC"]
print("\nGC Classification:")
for seq in test_seqs:
    print(f"  {seq}: {classify_gc(seq)}")

print("\n✓ Key concepts: if/elif/else, ==/</>/, and/or/not, validation")
