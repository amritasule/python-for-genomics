# Python for Genomics

A comprehensive Python toolkit for genomic data analysis and bioinformatics, created as part of the Coursera "Python for Genomic Data Science" course.

## 📚 Overview

This repository contains reusable Python modules and examples for working with DNA sequences, including:
- DNA sequence manipulation (complement, reverse complement, transcription)
- Sequence analysis (GC content, ORF finding, motif search)
- File format handling (FASTA, FASTQ)
- Translation and genetic code operations

## 🗂️ Repository Structure

```
python-for-genomics/
├── modules/               # Core reusable modules
│   ├── dna_tools.py      # Basic DNA operations
│   ├── sequence_analysis.py  # Advanced sequence analysis
│   └── file_parsers.py   # FASTA/FASTQ file handling
├── examples/             # Example scripts and workflows
│   ├── complete_analysis.py
│   ├── gc_content_analysis.py
│   └── orf_finder.py
├── data/                 # Sample data files
│   └── sample_sequences.fasta
├── tests/                # Unit tests (coming soon)
└── README.md            # This file
```

## 🚀 Quick Start

### Installation

Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/python-for-genomics.git
cd python-for-genomics
```

No external dependencies required! Uses only Python standard library.

### Basic Usage

```python
# Import the modules
import sys
sys.path.append('modules')

import dna_tools

# Analyze a DNA sequence
sequence = "ATGCGCTAGGGTAA"

# Calculate GC content
gc = dna_tools.gc_content(sequence)
print(f"GC Content: {gc:.2f}%")

# Get reverse complement
rev_comp = dna_tools.reverse_complement(sequence)
print(f"Reverse Complement: {rev_comp}")

# Translate to protein
protein = dna_tools.translate(sequence)
print(f"Protein: {protein}")
```

## 📖 Module Documentation

### dna_tools.py

Core DNA manipulation functions:

| Function | Description | Example |
|----------|-------------|---------|
| `validate_dna(seq)` | Check if sequence is valid DNA | `validate_dna("ATGC")` → `True` |
| `gc_content(seq)` | Calculate GC percentage | `gc_content("ATGC")` → `50.0` |
| `at_content(seq)` | Calculate AT percentage | `at_content("ATGC")` → `50.0` |
| `complement(seq)` | Get DNA complement | `complement("ATGC")` → `"TACG"` |
| `reverse_complement(seq)` | Get reverse complement | `reverse_complement("ATGC")` → `"GCAT"` |
| `transcribe(dna)` | Convert DNA to RNA | `transcribe("ATGC")` → `"AUGC"` |
| `translate(dna)` | Translate DNA to protein | `translate("ATGGCC")` → `"MA"` |
| `count_nucleotides(seq)` | Count each base | Returns dict of counts |
| `has_start_codon(seq)` | Check for ATG | Returns boolean |
| `has_stop_codon(seq)` | Check for stop codons | Returns boolean |

### sequence_analysis.py

Advanced analysis functions:

| Function | Description |
|----------|-------------|
| `find_motif(seq, motif)` | Find all occurrences of a pattern |
| `find_orfs(seq)` | Find open reading frames |
| `calculate_melting_temp(seq)` | Calculate Tm using Wallace rule |
| `gc_content_window(seq, size)` | GC content in sliding windows |
| `hamming_distance(seq1, seq2)` | Calculate Hamming distance |
| `find_repeats(seq, min_len)` | Find repeated sequences |

### file_parsers.py

File I/O functions:

| Function | Description |
|----------|-------------|
| `read_fasta(filename)` | Read FASTA file |
| `write_fasta(seqs, filename)` | Write FASTA file |
| `read_fastq(filename)` | Read FASTQ file |
| `write_fastq(records, filename)` | Write FASTQ file |

## 💡 Examples

### Example 1: Analyze a DNA Sequence

```python
import dna_tools
import sequence_analysis

sequence = "ATGCGCTAGGGTAAATGCCCTAGATGATG"

# Basic analysis
print(f"Length: {len(sequence)} bp")
print(f"GC Content: {dna_tools.gc_content(sequence):.2f}%")
print(f"Has start codon: {dna_tools.has_start_codon(sequence)}")

# Find ORFs
orfs = sequence_analysis.find_orfs(sequence)
print(f"ORFs found: {len(orfs)}")

# Translate
protein = dna_tools.translate(sequence)
print(f"Protein: {protein}")
```

### Example 2: Process FASTA File

```python
import file_parsers
import dna_tools

# Read FASTA file
sequences = file_parsers.read_fasta("data/sample_sequences.fasta")

# Analyze each sequence
for header, seq in sequences.items():
    gc = dna_tools.gc_content(seq)
    print(f"{header}: {len(seq)}bp, GC={gc:.1f}%")
```

### Example 3: Find ORFs in All Frames

```python
import sequence_analysis

sequence = "ATGCGCGCGTAGGGTAAATGATGCCCCCCTAG"

# Find ORFs in all three reading frames
for frame in range(3):
    frame_seq = sequence[frame:]
    orfs = sequence_analysis.find_orfs(frame_seq)
    print(f"Frame +{frame+1}: {len(orfs)} ORFs")
```

## 🧪 Running Examples

Run the provided example scripts:

```bash
# Complete analysis pipeline
cd examples
python complete_analysis.py

# GC content analysis
python gc_content_analysis.py

# ORF finder
python orf_finder.py
```

## 📊 Features

- ✅ No external dependencies (pure Python)
- ✅ Well-documented functions with docstrings
- ✅ Example scripts demonstrating common workflows
- ✅ FASTA/FASTQ file format support
- ✅ Complete genetic code table for translation
- ✅ ORF finding in all reading frames
- ✅ Sequence analysis tools (GC content, Tm, etc.)
- ✅ Pattern matching and motif finding

## 🎓 Learning Resources

This repository was created as part of learning Python for bioinformatics. Key concepts covered:

- **Python Basics**: Variables, data types, control flow
- **Functions**: Parameters, returns, scope
- **Data Structures**: Lists, dictionaries, strings
- **Modules**: Code organization and reusability
- **File I/O**: Reading and writing genomic file formats
- **Algorithms**: Pattern matching, ORF finding, sequence analysis

## 🔬 Use Cases

- **Education**: Learn bioinformatics programming
- **Research**: Quick sequence analysis and manipulation
- **Pipelines**: Building blocks for larger workflows
- **Prototyping**: Test ideas before using larger frameworks

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new features
- Improve documentation
- Report bugs
- Suggest enhancements

## 📝 License

MIT License - feel free to use this code for learning and research.

## 🙏 Acknowledgments

Created as part of the Coursera course "Python for Genomic Data Science" offered by Johns Hopkins University.

## 📞 Contact

Questions or suggestions? Open an issue or submit a pull request!

---

**Happy coding! 🧬**
