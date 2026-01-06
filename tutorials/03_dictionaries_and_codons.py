"""
TUTORIAL 3: Dictionaries and the Genetic Code
==============================================

Dictionaries are perfect for mapping codons to amino acids!
Learn key-value pairs through the genetic code.

Topics covered:
- Creating dictionaries
- Accessing values
- Adding/modifying entries
- Dictionary methods
- Looping through dictionaries
"""

print("="*70)
print("TUTORIAL 3: DICTIONARIES AND THE GENETIC CODE")
print("="*70)

# ============================================================================
# SECTION 1: Creating Dictionaries
# ============================================================================

print("\n" + "─"*70)
print("SECTION 1: Creating Dictionaries")
print("─"*70)

# Dictionary syntax: {key: value}
codon_table = {
    'ATG': 'Methionine',
    'TAA': 'Stop',
    'TAG': 'Stop',
    'TGA': 'Stop'
}

print("Simple codon table:")
print(codon_table)

# Creating with dict()
gene_info = dict(name='BRCA1', chromosome='17', length=81189)
print(f"\nGene info: {gene_info}")

# Empty dictionary
my_dict = {}
print(f"Empty dictionary: {my_dict}")

# ============================================================================
# SECTION 2: Accessing Dictionary Values
# ============================================================================

print("\n" + "─"*70)
print("SECTION 2: Accessing Values")
print("─"*70)

# Access with square brackets
amino_acid = codon_table['ATG']
print(f"ATG codes for: {amino_acid}")

# Safer access with .get()
amino_acid = codon_table.get('GGG', 'Unknown')
print(f"GGG codes for: {amino_acid}")

# Check if key exists
if 'ATG' in codon_table:
    print(f"✓ ATG is in the codon table")

if 'XXX' not in codon_table:
    print(f"✗ XXX is not a valid codon")

# ============================================================================
# SECTION 3: Adding and Modifying Entries
# ============================================================================

print("\n" + "─"*70)
print("SECTION 3: Adding and Modifying Entries")
print("─"*70)

# Start with small table
codons = {'ATG': 'Met'}
print(f"Initial: {codons}")

# Add new entry
codons['GCT'] = 'Ala'
print(f"After adding GCT: {codons}")

# Modify existing entry
codons['ATG'] = 'Methionine'  # Full name instead of abbreviation
print(f"After modifying ATG: {codons}")

# Add multiple entries
codons.update({'TAA': 'Stop', 'TAG': 'Stop', 'TGA': 'Stop'})
print(f"After update: {codons}")

# ============================================================================
# SECTION 4: Dictionary Methods
# ============================================================================

print("\n" + "─"*70)
print("SECTION 4: Dictionary Methods")
print("─"*70)

genetic_code = {
    'ATG': 'Met', 'GCT': 'Ala', 'GGG': 'Gly',
    'TAA': 'Stop', 'TAG': 'Stop'
}

# Get all keys
keys = genetic_code.keys()
print(f"All codons: {list(keys)}")

# Get all values
values = genetic_code.values()
print(f"All amino acids: {list(values)}")

# Get all items (key-value pairs)
items = genetic_code.items()
print(f"All items: {list(items)}")

# Remove an entry
removed = genetic_code.pop('TAG')
print(f"\nRemoved TAG: {removed}")
print(f"Remaining: {genetic_code}")

# Get dictionary length
print(f"Number of codons: {len(genetic_code)}")

# ============================================================================
# SECTION 5: Looping Through Dictionaries
# ============================================================================

print("\n" + "─"*70)
print("SECTION 5: Looping Through Dictionaries")
print("─"*70)

codon_table = {
    'ATG': 'Methionine',
    'GCT': 'Alanine',
    'GGG': 'Glycine',
    'TAA': 'Stop'
}

# Loop through keys
print("Looping through keys:")
for codon in codon_table:
    print(f"  {codon}")

# Loop through values
print("\nLooping through values:")
for amino_acid in codon_table.values():
    print(f"  {amino_acid}")

# Loop through key-value pairs (most common!)
print("\nLooping through key-value pairs:")
for codon, amino_acid in codon_table.items():
    print(f"  {codon} → {amino_acid}")

# ============================================================================
# SECTION 6: Nested Dictionaries
# ============================================================================

print("\n" + "─"*70)
print("SECTION 6: Nested Dictionaries")
print("─"*70)

# Dictionary of dictionaries
genes = {
    'BRCA1': {
        'chromosome': '17',
        'start': 43044295,
        'end': 43170245,
        'function': 'DNA repair'
    },
    'TP53': {
        'chromosome': '17',
        'start': 7661779,
        'end': 7687550,
        'function': 'Tumor suppressor'
    }
}

print("Gene database:")
for gene_name, gene_data in genes.items():
    print(f"\n{gene_name}:")
    for key, value in gene_data.items():
        print(f"  {key}: {value}")

# ============================================================================
# SECTION 7: Counting with Dictionaries
# ============================================================================

print("\n" + "─"*70)
print("SECTION 7: Counting with Dictionaries")
print("─"*70)

def count_bases(sequence):
    """Count each base in a sequence using a dictionary."""
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    
    for base in sequence:
        if base in counts:
            counts[base] += 1
    
    return counts

dna = "ATGCGCTAGGGTAA"
base_counts = count_bases(dna)

print(f"Sequence: {dna}")
print(f"Base counts:")
for base, count in base_counts.items():
    print(f"  {base}: {count}")

# ============================================================================
# SECTION 8: Building a Genetic Code Dictionary
# ============================================================================

print("\n" + "─"*70)
print("SECTION 8: Complete Genetic Code Table")
print("─"*70)

# Complete genetic code
genetic_code = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def translate_dna(dna, genetic_code):
    """Translate DNA to protein using genetic code dictionary."""
    protein = ""
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        amino_acid = genetic_code.get(codon, 'X')
        if amino_acid == '*':
            break
        protein += amino_acid
    return protein

# Test translation
test_dna = "ATGCGCGCGTAGGGTAA"
protein = translate_dna(test_dna, genetic_code)
print(f"DNA: {test_dna}")
print(f"Protein: {protein}")

# ============================================================================
# SECTION 9: Dictionary Comprehension
# ============================================================================

print("\n" + "─"*70)
print("SECTION 9: Dictionary Comprehension")
print("─"*70)

# Create dictionary from sequence
sequence = "ATGCGC"
base_to_index = {base: i for i, base in enumerate(sequence)}
print(f"Base positions: {base_to_index}")

# Count codons in a sequence
dna = "ATGCGCTAGATGGGGATGTAA"
codons = [dna[i:i+3] for i in range(0, len(dna)-2, 3)]
codon_counts = {codon: codons.count(codon) for codon in set(codons)}
print(f"\nCodon counts in {dna}:")
for codon, count in codon_counts.items():
    print(f"  {codon}: {count}")

# ============================================================================
# TRY IT YOURSELF
# ============================================================================

print("\n" + "="*70)
print("TRY IT YOURSELF")
print("="*70)

print("""
1. Create a dictionary mapping gene names to their functions
2. Add a new gene to the dictionary
3. Loop through and print all genes
4. Count how many times each codon appears in a DNA sequence
5. Build a reverse genetic code (amino acid → codons)

Try modifying the code above to practice!
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("="*70)
print("KEY TAKEAWAYS")
print("="*70)

print("""
✓ Dictionaries map keys to values: {key: value}
✓ Perfect for genetic code (codon → amino acid)
✓ Access with dict[key] or dict.get(key, default)
✓ Add/modify: dict[key] = value
✓ Loop with .items() to get both key and value
✓ Check membership with 'in'
✓ Methods: .keys(), .values(), .items(), .get(), .pop()
✓ Dictionaries are mutable (can be changed)
""")

print("\n✨ Next: Tutorial 4 - Conditionals in Genomics\n")
