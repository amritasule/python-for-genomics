"""
Complete Genomic Analysis Pipeline
Demonstrates using all modules together
"""

import sys
sys.path.append('../modules')

import dna_tools
import sequence_analysis
import file_parsers


def analyze_sequence(name, sequence):
    """
    Perform complete analysis on a sequence.
    """
    print(f"\n{'='*60}")
    print(f"Analysis for: {name}")
    print(f"{'='*60}")
    
    # Basic properties
    print(f"\nSequence: {sequence}")
    print(f"Length: {len(sequence)} bp")
    
    # Validation
    if not dna_tools.validate_dna(sequence):
        print("WARNING: Invalid DNA sequence!")
        return
    
    # Composition
    print(f"\nComposition:")
    counts = dna_tools.count_nucleotides(sequence)
    for base, count in counts.items():
        print(f"  {base}: {count} ({count/len(sequence)*100:.1f}%)")
    
    print(f"\nGC Content: {dna_tools.gc_content(sequence):.2f}%")
    print(f"AT Content: {dna_tools.at_content(sequence):.2f}%")
    
    # Melting temperature
    tm = sequence_analysis.calculate_melting_temp(sequence)
    print(f"Melting Temperature: {tm}°C")
    
    # Complements
    print(f"\nComplement: {dna_tools.complement(sequence)}")
    print(f"Reverse Complement: {dna_tools.reverse_complement(sequence)}")
    
    # Transcription
    rna = dna_tools.transcribe(sequence)
    print(f"\nRNA: {rna}")
    
    # Codons
    print(f"\nStart codon (ATG): {'Yes' if dna_tools.has_start_codon(sequence) else 'No'}")
    print(f"Stop codon: {'Yes' if dna_tools.has_stop_codon(sequence) else 'No'}")
    
    # ORFs
    orfs = sequence_analysis.find_orfs(sequence)
    if orfs:
        print(f"\nOpen Reading Frames: {len(orfs)}")
        for i, (start, end, orf) in enumerate(orfs, 1):
            protein = dna_tools.translate(orf)
            print(f"  ORF {i}: Position {start}-{end}")
            print(f"    DNA: {orf}")
            print(f"    Protein: {protein}")
    else:
        print("\nNo complete ORFs found")
    
    # Motif search
    atg_positions = sequence_analysis.find_motif(sequence, "ATG")
    if atg_positions:
        print(f"\nATG occurrences at positions: {atg_positions}")


def main():
    """
    Main analysis pipeline.
    """
    print("GENOMIC SEQUENCE ANALYSIS PIPELINE")
    print("="*60)
    
    # Example sequences
    sequences = {
        "Example Gene 1": "ATGCGCTAGGGCTAAGGGTAG",
        "Example Gene 2": "ATGATGCCCTAGATGATGTAGGGTAA",
        "Short Sequence": "ATGC"
    }
    
    # Analyze each sequence
    for name, seq in sequences.items():
        analyze_sequence(name, seq)
    
    # Example: Working with FASTA files
    print(f"\n{'='*60}")
    print("FASTA FILE EXAMPLE")
    print(f"{'='*60}")
    
    # Create sample FASTA
    file_parsers.write_fasta(sequences, "analysis_results.fasta")
    print("\nWrote sequences to: analysis_results.fasta")
    
    # Read it back
    loaded_sequences = file_parsers.read_fasta("analysis_results.fasta")
    print(f"Loaded {len(loaded_sequences)} sequences from file")
    
    print("\n" + "="*60)
    print("Analysis complete!")
    print("="*60)


if __name__ == "__main__":
    main()
