"""
PRACTICE EXERCISE SOLUTIONS
============================

Solutions to the practice exercises.
Study these after attempting the exercises yourself!
"""

print("="*70)
print("PYTHON FOR GENOMICS - EXERCISE SOLUTIONS")
print("="*70)

# ============================================================================
# DATA STRUCTURES SOLUTIONS
# ============================================================================

print("\n" + "="*70)
print("DATA STRUCTURES SOLUTIONS")
print("="*70)

# EXERCISE 1: Base Counter
print("\nSOLUTION 1: Base Counter")
print("─"*40)

def count_bases(sequence):
    """Count each base in a DNA sequence."""
    sequence = sequence.upper()
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    
    for base in sequence:
        if base in counts:
            counts[base] += 1
    
    return counts

# Test
test_seq = "ATGCGCTAGGGTAA"
result = count_bases(test_seq)
print(f"count_bases('{test_seq}')")
print(f"Result: {result}")

# ============================================================================

# EXERCISE 2: Codon Extractor
print("\nSOLUTION 2: Codon Extractor")
print("─"*40)

def extract_codons(sequence):
    """Extract all codons from a DNA sequence."""
    codons = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        codons.append(codon)
    return codons

# Alternative: List comprehension
def extract_codons_v2(sequence):
    """Extract codons using list comprehension."""
    return [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]

# Test
test_seq = "ATGCGCTAGGGTAA"
result = extract_codons(test_seq)
print(f"extract_codons('{test_seq}')")
print(f"Result: {result}")

# ============================================================================

# EXERCISE 3: Reverse Complement
print("\nSOLUTION 3: Reverse Complement")
print("─"*40)

def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Get complement
    complement = ""
    for base in sequence.upper():
        complement += complement_map[base]
    
    # Reverse it
    return complement[::-1]

# Alternative: More compact
def reverse_complement_v2(sequence):
    """Reverse complement in one line."""
    comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([comp[base] for base in sequence.upper()])[::-1]

# Test
test_seq = "ATGCGC"
result = reverse_complement(test_seq)
print(f"reverse_complement('{test_seq}')")
print(f"Result: {result}")

# ============================================================================
# CONDITIONALS SOLUTIONS
# ============================================================================

print("\n" + "="*70)
print("CONDITIONALS SOLUTIONS")
print("="*70)

# EXERCISE 4: Sequence Validator
print("\nSOLUTION 4: Sequence Validator")
print("─"*40)

def is_valid_dna(sequence):
    """Check if sequence contains only valid DNA bases."""
    valid_bases = set('ATGC')
    sequence_bases = set(sequence.upper())
    return sequence_bases.issubset(valid_bases)

# Alternative: Using a loop
def is_valid_dna_v2(sequence):
    """Check validity using a loop."""
    for base in sequence.upper():
        if base not in 'ATGC':
            return False
    return True

# Test
print(f"is_valid_dna('ATGC') → {is_valid_dna('ATGC')}")
print(f"is_valid_dna('ATXC') → {is_valid_dna('ATXC')}")

# ============================================================================

# EXERCISE 5: GC Classifier
print("\nSOLUTION 5: GC Classifier")
print("─"*40)

def classify_gc(sequence):
    """Classify sequence by GC content."""
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    gc_percent = (gc_count / len(sequence)) * 100
    
    if gc_percent > 60:
        return "GC-rich"
    elif gc_percent >= 40:
        return "Moderate"
    else:
        return "AT-rich"

# Test
print(f"classify_gc('GCGCGC') → {classify_gc('GCGCGC')}")
print(f"classify_gc('ATATATAT') → {classify_gc('ATATATAT')}")

# ============================================================================

# EXERCISE 6: ORF Checker
print("\nSOLUTION 6: ORF Checker")
print("─"*40)

def is_valid_orf(sequence):
    """Check if sequence is a valid ORF."""
    sequence = sequence.upper()
    
    # Check start codon
    has_start = sequence.startswith('ATG')
    
    # Check stop codon
    stop_codons = ['TAA', 'TAG', 'TGA']
    has_stop = sequence.endswith(tuple(stop_codons))
    
    # Check length divisible by 3
    divisible_by_3 = len(sequence) % 3 == 0
    
    return has_start and has_stop and divisible_by_3

# Test
print(f"is_valid_orf('ATGCGCTAG') → {is_valid_orf('ATGCGCTAG')}")
print(f"is_valid_orf('GCGCGCTAG') → {is_valid_orf('GCGCGCTAG')}")

# ============================================================================
# LOOPS SOLUTIONS
# ============================================================================

print("\n" + "="*70)
print("LOOPS SOLUTIONS")
print("="*70)

# EXERCISE 7: Pattern Finder
print("\nSOLUTION 7: Pattern Finder")
print("─"*40)

def find_motif(sequence, motif):
    """Find all positions of a motif in a sequence."""
    positions = []
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            positions.append(i)
    return positions

# Test
test_seq = "ATGCATGATG"
test_motif = "ATG"
result = find_motif(test_seq, test_motif)
print(f"find_motif('{test_seq}', '{test_motif}')")
print(f"Result: {result}")

# ============================================================================

# EXERCISE 8: Sequence Comparer
print("\nSOLUTION 8: Sequence Comparer")
print("─"*40)

def calculate_similarity(seq1, seq2):
    """Calculate percentage of matching bases."""
    if len(seq1) != len(seq2):
        return None
    
    matches = 0
    for base1, base2 in zip(seq1, seq2):
        if base1 == base2:
            matches += 1
    
    return (matches / len(seq1)) * 100

# Alternative: List comprehension
def calculate_similarity_v2(seq1, seq2):
    """Calculate similarity using comprehension."""
    if len(seq1) != len(seq2):
        return None
    matches = sum(1 for b1, b2 in zip(seq1, seq2) if b1 == b2)
    return (matches / len(seq1)) * 100

# Test
result = calculate_similarity('ATGC', 'ATCC')
print(f"calculate_similarity('ATGC', 'ATCC')")
print(f"Result: {result}%")

# ============================================================================

# EXERCISE 9: Multiple Frame ORF Finder
print("\nSOLUTION 9: Multiple Frame ORF Finder")
print("─"*40)

def find_orfs_all_frames(sequence):
    """Find all ORFs in all three reading frames."""
    orfs = []
    
    # Check all three reading frames
    for frame in range(3):
        frame_seq = sequence[frame:]
        
        # Find all ATG positions
        for i in range(0, len(frame_seq) - 2, 3):
            codon = frame_seq[i:i+3]
            if codon == 'ATG':
                # Found start, look for stop
                for j in range(i + 3, len(frame_seq) - 2, 3):
                    stop_codon = frame_seq[j:j+3]
                    if stop_codon in ['TAA', 'TAG', 'TGA']:
                        orf = frame_seq[i:j+3]
                        actual_pos = i + frame
                        orfs.append((frame, actual_pos, orf))
                        break
    
    return orfs

# Test
test_seq = "ATGCGCTAGATGGGGTAA"
result = find_orfs_all_frames(test_seq)
print(f"find_orfs_all_frames('{test_seq}')")
for frame, pos, orf in result:
    print(f"  Frame {frame}, Position {pos}: {orf}")

# ============================================================================
# FILE I/O SOLUTIONS
# ============================================================================

print("\n" + "="*70)
print("FILE I/O SOLUTIONS")
print("="*70)

# EXERCISE 10: FASTA Reader
print("\nSOLUTION 10: FASTA Reader")
print("─"*40)

def read_fasta(filename):
    """Read a FASTA file and return dictionary of sequences."""
    sequences = {}
    current_header = None
    current_seq = ""
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                
                if line.startswith('>'):
                    # Save previous sequence
                    if current_header:
                        sequences[current_header] = current_seq
                    
                    # Start new sequence
                    current_header = line[1:]
                    current_seq = ""
                else:
                    # Add to current sequence
                    current_seq += line
            
            # Save last sequence
            if current_header:
                sequences[current_header] = current_seq
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return {}
    
    return sequences

# Test
import os
if os.path.exists('../data/sample_sequences.fasta'):
    result = read_fasta('../data/sample_sequences.fasta')
    print(f"Read {len(result)} sequences")
    for header in list(result.keys())[:2]:
        print(f"  {header[:50]}...")

# ============================================================================

# EXERCISE 11: Sequence Filter
print("\nSOLUTION 11: Sequence Filter")
print("─"*40)

def filter_by_length(input_file, output_file, min_length):
    """Filter sequences by minimum length."""
    # Read sequences
    sequences = read_fasta(input_file)
    
    # Filter
    filtered = {header: seq for header, seq in sequences.items() 
                if len(seq) >= min_length}
    
    # Write filtered sequences
    with open(output_file, 'w') as file:
        for header, seq in filtered.items():
            file.write(f">{header}\n")
            # Write sequence in 60-character lines
            for i in range(0, len(seq), 60):
                file.write(seq[i:i+60] + "\n")
    
    print(f"Filtered {len(filtered)}/{len(sequences)} sequences")
    print(f"Saved to {output_file}")

# Test
print("filter_by_length example shown (requires input file)")

# ============================================================================

# EXERCISE 12: FASTA Merger
print("\nSOLUTION 12: FASTA Merger")
print("─"*40)

def merge_fasta_files(input_files, output_file):
    """Merge multiple FASTA files into one."""
    all_sequences = {}
    
    # Read all files
    for filename in input_files:
        sequences = read_fasta(filename)
        all_sequences.update(sequences)
    
    # Write merged file
    with open(output_file, 'w') as file:
        for header, seq in all_sequences.items():
            file.write(f">{header}\n")
            for i in range(0, len(seq), 60):
                file.write(seq[i:i+60] + "\n")
    
    print(f"Merged {len(all_sequences)} sequences from {len(input_files)} files")
    print(f"Saved to {output_file}")

# Test
print("merge_fasta_files example shown (requires input files)")

# ============================================================================

print("\n" + "="*70)
print("ALL SOLUTIONS COMPLETE!")
print("="*70)
print("\nKey takeaways:")
print("✓ Multiple ways to solve the same problem")
print("✓ List comprehensions can make code more compact")
print("✓ Always handle errors (try-except, file checks)")
print("✓ Test your code with example inputs")
print("\nKeep practicing! 🧬")
