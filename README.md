# Python for Genomics

A comprehensive Python toolkit for genomic data analysis and bioinformatics, created as part of the Coursera "Python for Genomic Data Science" course.

## 📚 Overview

This repository provides everything you need to learn Python for genomics:
- **Tutorials** - Learn Python fundamentals with genomics examples
- **Modules** - Reusable tools for DNA/RNA analysis
- **Examples** - Complete genomics workflows
- **Practice** - Exercises to test your skills
- **Quick Reference** - Fast lookup cheat sheet

## 🗂️ Repository Structure

```
python-for-genomics/
├── tutorials/            # 📗 Python fundamentals (START HERE!)
│   ├── 01_strings_and_dna.py
│   ├── 02_lists_and_sequences.py
│   ├── 03_dictionaries_and_codons.py
│   ├── 04_conditionals_in_genomics.py
│   ├── 05_loops_and_iteration.py
│   └── 06_file_io_genomics.py
├── modules/              # Core reusable modules
│   ├── dna_tools.py
│   ├── sequence_analysis.py
│   └── file_parsers.py
├── examples/             # Complete genomics workflows
│   ├── 00_basic_operations.py
│   ├── 01_my_first_analysis.py
│   ├── 02_interactive_analyzer.py
│   ├── 03_compare_sequences.py
│   ├── 04_gc_content_analysis.py
│   ├── 05_orf_finder.py
│   └── 06_fasta_file_operations.py
├── practice/             # 💪 Test your skills
│   ├── exercises.py
│   └── solutions.py
├── data/                 # Sample data files
├── QUICK_REFERENCE.md    # 📖 Cheat sheet
└── README.md
```

## 🚀 Getting Started

### For Complete Beginners

**Start with the tutorials!** They teach Python fundamentals using genomics examples.

```bash
cd tutorials
python3 01_strings_and_dna.py
```

Work through tutorials 01-06 in order. Each tutorial is a complete, runnable script with explanations.

### For Those Who Know Python

Jump straight to the examples to see complete genomics workflows:

```bash
cd examples
python3 00_basic_operations.py
```

## 📚 Learning Path

### Step 1: Fundamentals (tutorials/)

Learn Python basics with genomics context:

1. **Strings and DNA** - String operations for sequences
2. **Lists** - Working with multiple sequences
3. **Dictionaries** - Genetic code and mappings
4. **Conditionals** - Sequence validation
5. **Loops** - Iterating through data
6. **File I/O** - Reading and writing FASTA files

Each tutorial includes:
- Clear explanations
- Code examples
- Genomics applications
- Try-it-yourself exercises

### Step 2: Examples (examples/)

See complete workflows in action:

📗 **Beginner**
- 00: Basic DNA operations
- 01: Your first analysis
- 02: Interactive analyzer
- 03: Compare sequences

📙 **Intermediate**
- 04: GC content analysis
- 05: ORF finding

📕 **Advanced**
- 06: Complete FASTA operations

### Step 3: Practice (practice/)

Test your skills with exercises:
- 12 exercises covering all concepts
- Solutions provided
- Real genomics problems

### Step 4: Reference (QUICK_REFERENCE.md)

Fast lookup for Python syntax and common patterns.

## 💻 Installation

```bash
git clone https://github.com/amritasule/python-for-genomics.git
cd python-for-genomics
```

No external dependencies! Uses only Python standard library.

## 📖 Module Documentation

### dna_tools.py - Core DNA Functions

| Function | Description |
|----------|-------------|
| `validate_dna(seq)` | Check if valid DNA |
| `gc_content(seq)` | Calculate GC percentage |
| `complement(seq)` | Get DNA complement |
| `reverse_complement(seq)` | Get reverse complement |
| `transcribe(dna)` | Convert DNA to RNA |
| `translate(dna)` | Translate to protein |
| `count_nucleotides(seq)` | Count each base |
| `has_start_codon(seq)` | Check for ATG |
| `has_stop_codon(seq)` | Check for stop codons |

### sequence_analysis.py - Advanced Analysis

| Function | Description |
|----------|-------------|
| `find_motif(seq, motif)` | Find pattern occurrences |
| `find_orfs(seq)` | Find open reading frames |
| `calculate_melting_temp(seq)` | Calculate Tm |
| `hamming_distance(seq1, seq2)` | Calculate differences |
| `gc_content_window(seq, size)` | Sliding window GC |
| `find_repeats(seq, min_len)` | Find repeated sequences |

### file_parsers.py - File I/O

| Function | Description |
|----------|-------------|
| `read_fasta(filename)` | Read FASTA file |
| `write_fasta(seqs, filename)` | Write FASTA file |
| `read_fastq(filename)` | Read FASTQ file |
| `write_fastq(records, filename)` | Write FASTQ file |

## 🎯 Quick Start Examples

### Analyze a sequence

```python
import sys
sys.path.append('modules')
import dna_tools

sequence = "ATGCGCTAGGGTAA"
print(f"GC Content: {dna_tools.gc_content(sequence):.2f}%")
print(f"Protein: {dna_tools.translate(sequence)}")
```

### Read FASTA file

```python
import file_parsers

sequences = file_parsers.read_fasta('data/sample_sequences.fasta')
for header, seq in sequences.items():
    print(f"{header}: {len(seq)} bp")
```

### Find ORFs

```python
import sequence_analysis

orfs = sequence_analysis.find_orfs("ATGCGCGCGTAGGGTAA")
for start, end, orf in orfs:
    print(f"ORF: {orf}")
```

## ✨ Features

- ✅ No external dependencies (pure Python)
- ✅ Complete tutorials with genomics examples
- ✅ Runnable code examples
- ✅ Practice exercises with solutions
- ✅ FASTA/FASTQ file support
- ✅ Complete genetic code table
- ✅ ORF finding in all reading frames
- ✅ Quick reference guide
- ✅ Portfolio-ready quality

## 🎓 Topics Covered

### Python Fundamentals
- Variables and data types
- Strings, lists, dictionaries
- If/elif/else statements
- For and while loops
- Functions and modules
- File I/O operations

### Bioinformatics Concepts
- DNA sequence manipulation
- GC content calculation
- Sequence complement
- Transcription and translation
- ORF finding
- FASTA file parsing
- Sequence comparison
- Pattern matching

## 🔬 Use Cases

- **Education** - Learn Python and bioinformatics
- **Research** - Quick sequence analysis
- **Pipelines** - Building blocks for workflows
- **Prototyping** - Test ideas before scaling

## 📝 Examples of What You Can Do

After completing the tutorials, you'll be able to:

✓ Analyze DNA sequences (GC content, composition, etc.)  
✓ Read and write FASTA files  
✓ Find open reading frames (ORFs)  
✓ Translate DNA to protein  
✓ Compare sequences  
✓ Filter sequences by criteria  
✓ Search for patterns and motifs  
✓ Build analysis pipelines  

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new features
- Improve documentation
- Report bugs
- Suggest enhancements

## 📞 Resources

- **tutorials/README.md** - Detailed tutorial guide
- **practice/README.md** - Exercise instructions
- **QUICK_REFERENCE.md** - Python syntax cheat sheet
- **examples/** - Working code examples

## 🙏 Acknowledgments

Created as part of the Coursera course "Python for Genomic Data Science" offered by Johns Hopkins University.

## 📝 License

MIT License - feel free to use this code for learning and research.

---

**Ready to start? Head to tutorials/ and begin with 01_strings_and_dna.py!**

**Happy coding! 🧬**
