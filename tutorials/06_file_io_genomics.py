"""
TUTORIAL 6: File I/O in Genomics
=================================

Learn to read and write genomic data files!

Topics covered:
- Opening and closing files
- Reading files (read, readline, readlines)
- Writing files
- File modes (r, w, a)
- Working with FASTA files
- Error handling with files
"""

print("="*70)
print("TUTORIAL 6: FILE I/O IN GENOMICS")
print("="*70)

import sys
sys.path.append('../modules')

# ============================================================================
# SECTION 1: Opening and Closing Files
# ============================================================================

print("\n" + "─"*70)
print("SECTION 1: Opening and Closing Files")
print("─"*70)

print("""
File modes:
  'r'  - Read (default) - Error if file doesn't exist
  'w'  - Write - Creates new or OVERWRITES existing
  'a'  - Append - Creates new or adds to existing
  'r+' - Read and write - Error if doesn't exist
""")

# Method 1: Manual open and close
print("\nMethod 1: Manual open/close")
print("file = open('data.txt', 'r')")
print("content = file.read()")
print("file.close()  # IMPORTANT!")

# Method 2: With statement (RECOMMENDED!)
print("\nMethod 2: With statement (automatic close)")
print("with open('data.txt', 'r') as file:")
print("    content = file.read()")
print("# File automatically closed!")

# ============================================================================
# SECTION 2: Reading Files
# ============================================================================

print("\n" + "─"*70)
print("SECTION 2: Reading Files")
print("─"*70)

# Create a sample file first
with open('sample_sequence.txt', 'w') as f:
    f.write("ATGCGCTAGGGTAA\n")
    f.write("GCTAGCTAGCTA\n")
    f.write("CGCGCGCGTAG\n")

print("Created sample_sequence.txt")

# Method 1: read() - reads entire file as one string
print("\n1. Using read():")
with open('sample_sequence.txt', 'r') as file:
    content = file.read()
    print(f"Content:\n{content}")

# Method 2: readline() - reads one line at a time
print("\n2. Using readline():")
with open('sample_sequence.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# Method 3: readlines() - reads all lines into a list
print("\n3. Using readlines():")
with open('sample_sequence.txt', 'r') as file:
    lines = file.readlines()
    print(f"All lines: {lines}")
    print(f"Number of lines: {len(lines)}")

# Method 4: Loop through file (BEST for large files!)
print("\n4. Looping through file:")
with open('sample_sequence.txt', 'r') as file:
    for i, line in enumerate(file, 1):
        seq = line.strip()
        print(f"  Sequence {i}: {seq} ({len(seq)} bp)")

# ============================================================================
# SECTION 3: Writing Files
# ============================================================================

print("\n" + "─"*70)
print("SECTION 3: Writing Files")
print("─"*70)

# Write mode - creates new or overwrites
print("Writing to output.txt...")
with open('output.txt', 'w') as file:
    file.write("Sequence Analysis Results\n")
    file.write("=" * 30 + "\n")
    file.write("Sequence: ATGCGC\n")
    file.write("Length: 6 bp\n")
    file.write("GC Content: 66.7%\n")

print("✓ File written!")

# Append mode - adds to existing file
print("\nAppending to output.txt...")
with open('output.txt', 'a') as file:
    file.write("\nAdditional Analysis:\n")
    file.write("Has start codon: Yes\n")

print("✓ Content appended!")

# Read and display the file
print("\nContents of output.txt:")
with open('output.txt', 'r') as file:
    print(file.read())

# ============================================================================
# SECTION 4: Reading FASTA Files
# ============================================================================

print("\n" + "─"*70)
print("SECTION 4: Reading FASTA Files")
print("─"*70)

# Create a sample FASTA file
fasta_content = """>gene1 Example sequence
ATGCGCTAGGGTAA
GCTAGCTAGCTA
>gene2 Another sequence
CGCGCGCGTAG
"""

with open('sample.fasta', 'w') as f:
    f.write(fasta_content)

print("Created sample.fasta")

# Simple FASTA reader
def read_fasta_simple(filename):
    """Simple FASTA file reader."""
    sequences = {}
    current_header = None
    current_seq = ""
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line.startswith('>'):
                # Save previous sequence
                if current_header:
                    sequences[current_header] = current_seq
                
                # Start new sequence
                current_header = line[1:]  # Remove '>'
                current_seq = ""
            else:
                # Add to current sequence
                current_seq += line
        
        # Save last sequence
        if current_header:
            sequences[current_header] = current_seq
    
    return sequences

# Test it
print("\nReading FASTA file:")
seqs = read_fasta_simple('sample.fasta')
for header, seq in seqs.items():
    print(f"  {header}")
    print(f"    Sequence: {seq}")
    print(f"    Length: {len(seq)} bp")

# ============================================================================
# SECTION 5: Writing FASTA Files
# ============================================================================

print("\n" + "─"*70)
print("SECTION 5: Writing FASTA Files")
print("─"*70)

def write_fasta_simple(sequences, filename, line_length=60):
    """Simple FASTA file writer."""
    with open(filename, 'w') as file:
        for header, seq in sequences.items():
            # Write header
            file.write(f">{header}\n")
            
            # Write sequence in wrapped lines
            for i in range(0, len(seq), line_length):
                file.write(seq[i:i+line_length] + "\n")

# Create sequences to write
output_seqs = {
    'sequence1 | GC-rich': 'GCGCGCGCGCGCGCGC',
    'sequence2 | AT-rich': 'ATATATATATATATAT'
}

print("Writing output.fasta...")
write_fasta_simple(output_seqs, 'output.fasta')
print("✓ FASTA file written!")

# Read and display it
print("\nContents of output.fasta:")
with open('output.fasta', 'r') as file:
    print(file.read())

# ============================================================================
# SECTION 6: File Operations
# ============================================================================

print("\n" + "─"*70)
print("SECTION 6: File Operations")
print("─"*70)

# Check if file exists
import os

filename = 'sample.fasta'
if os.path.exists(filename):
    print(f"✓ {filename} exists")
    
    # Get file size
    size = os.path.getsize(filename)
    print(f"  Size: {size} bytes")
else:
    print(f"✗ {filename} does not exist")

# List all .fasta files
print("\nFASTA files in current directory:")
for file in os.listdir('.'):
    if file.endswith('.fasta'):
        print(f"  {file}")

# ============================================================================
# SECTION 7: Error Handling
# ============================================================================

print("\n" + "─"*70)
print("SECTION 7: Error Handling")
print("─"*70)

# Try to read a file that doesn't exist
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("✗ Error: File not found!")

# Better: Check if file exists first
filename = 'nonexistent.txt'
if os.path.exists(filename):
    with open(filename, 'r') as file:
        content = file.read()
else:
    print(f"✗ {filename} does not exist")

# ============================================================================
# SECTION 8: Practical Example - Sequence Filter
# ============================================================================

print("\n" + "─"*70)
print("SECTION 8: Practical Example - Sequence Filter")
print("─"*70)

def filter_sequences_by_gc(input_file, output_file, min_gc=40):
    """Filter sequences by GC content."""
    print(f"Filtering sequences with GC ≥ {min_gc}%...")
    
    # Read sequences
    sequences = read_fasta_simple(input_file)
    filtered = {}
    
    # Filter
    for header, seq in sequences.items():
        gc_count = seq.count('G') + seq.count('C')
        gc_percent = (gc_count / len(seq)) * 100
        
        if gc_percent >= min_gc:
            filtered[header] = seq
            print(f"  ✓ {header}: GC={gc_percent:.1f}%")
        else:
            print(f"  ✗ {header}: GC={gc_percent:.1f}% (filtered out)")
    
    # Write filtered sequences
    write_fasta_simple(filtered, output_file)
    print(f"\n✓ Wrote {len(filtered)} sequences to {output_file}")

# Test
filter_sequences_by_gc('sample.fasta', 'filtered.fasta', min_gc=50)

# ============================================================================
# SECTION 9: Command-Line Arguments
# ============================================================================

print("\n" + "─"*70)
print("SECTION 9: Command-Line Arguments")
print("─"*70)

print("""
Using sys.argv to get command-line arguments:

import sys

# Script: analyze.py
# Run: python analyze.py input.fasta output.txt

input_file = sys.argv[1]   # 'input.fasta'
output_file = sys.argv[2]  # 'output.txt'

sys.argv[0] is always the script name
sys.argv[1], sys.argv[2], etc. are the arguments
""")

# ============================================================================
# TRY IT YOURSELF
# ============================================================================

print("\n" + "="*70)
print("TRY IT YOURSELF")
print("="*70)

print("""
1. Read a FASTA file and count total sequences
2. Filter sequences by length
3. Convert a file to uppercase
4. Merge multiple FASTA files into one
5. Extract sequences containing a specific motif

Try creating your own file processing scripts!
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("="*70)
print("KEY TAKEAWAYS")
print("="*70)

print("""
✓ Always use 'with open()' - it closes files automatically
✓ 'r' mode for reading (error if doesn't exist)
✓ 'w' mode for writing (overwrites existing!)
✓ 'a' mode for appending (adds to existing)
✓ readline() for one line, readlines() for all lines
✓ Loop through file for memory efficiency
✓ FASTA: Header starts with >, sequence on following lines
✓ Use try-except for error handling
✓ Check os.path.exists() before opening
""")

print("\n✨ Congratulations! You've completed all tutorials!\n")
print("Next steps:")
print("  - Check out the examples/ directory")
print("  - Try the practice/ exercises")
print("  - Use QUICK_REFERENCE.md for quick lookups")
print("\nHappy coding! 🧬")
