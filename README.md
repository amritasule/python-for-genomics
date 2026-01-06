# Python for Genomics

A comprehensive Python toolkit for genomic data analysis and bioinformatics, created as part of the Coursera "Python for Genomic Data Science" course.

## Overview

This repository contains reusable Python modules and examples for working with DNA sequences, including:
- DNA sequence manipulation (complement, reverse complement, transcription)
- Sequence analysis (GC content, ORF finding, motif search)
- File format handling (FASTA, FASTQ)
- Translation and genetic code operations

## Quick Start

Clone the repository:
```bash
git clone https://github.com/amritasule/python-for-genomics.git
cd python-for-genomics
```

No external dependencies required!

## Examples by Difficulty

### Beginner (Start Here!)

**00_basic_operations.py** - The simplest example
- Shows each function one at a time
- Perfect for learning

**01_my_first_analysis.py** - Your first DNA analysis
- Step-by-step walkthrough
- All basic operations together

### Beginner-Intermediate

**02_interactive_analyzer.py** - Interactive sequence input
- Type your own DNA sequences
- Great for experimenting!

**03_compare_sequences.py** - Compare two sequences
- See how sequences differ
- Find mutations

### 📙 Intermediate

**04_gc_content_analysis.py** - GC content visualization
- Sliding window analysis
- Compare GC-rich vs AT-rich sequences
- Statistical analysis

### 📕 Advanced

**05_orf_finder.py** - Open Reading Frame detection
- Find potential genes
- Analyze all reading frames
- Translate to proteins

## Learning Path

New to Python? Follow this order:
1. Start with 00_basic_operations.py
2. Try 01_my_first_analysis.py
3. Experiment with 02_interactive_analyzer.py
4. Move on to intermediate examples

## Module Documentation

### dna_tools.py - Core DNA Functions

- validate_dna(seq) - Check if valid DNA
- gc_content(seq) - Calculate GC percentage
- complement(seq) - Get DNA complement
- reverse_complement(seq) - Get reverse complement
- transcribe(dna) - Convert DNA to RNA
- translate(dna) - Translate to protein
- count_nucleotides(seq) - Count each base
- has_start_codon(seq) - Check for ATG
- has_stop_codon(seq) - Check for stop codons

### sequence_analysis.py - Advanced Analysis

- find_motif(seq, motif) - Find pattern occurrences
- find_orfs(seq) - Find open reading frames
- calculate_melting_temp(seq) - Calculate Tm
- hamming_distance(seq1, seq2) - Calculate differences

### file_parsers.py - File I/O

- read_fasta(filename) - Read FASTA file
- write_fasta(seqs, filename) - Write FASTA file

## Features

- No external dependencies (pure Python)
- Well-documented functions
- Examples for all skill levels
- FASTA/FASTQ file support
- Interactive learning examples

## Acknowledgments

Created as part of the Coursera course "Python for Genomic Data Science" by Johns Hopkins University.

Happy coding!
