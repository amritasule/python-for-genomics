"""
File Parsers Module
Functions for reading and writing genomic file formats
"""


def read_fasta(filename):
    """
    Read sequences from FASTA file.
    
    Args:
        filename (str): Path to FASTA file
        
    Returns:
        dict: Dictionary of {header: sequence}
        
    Example FASTA format:
        >seq1
        ATGCGCTAGGC
        TAGGCTA
        >seq2
        GCTAGCTA
    """
    sequences = {}
    current_header = None
    current_sequence = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('>'):
                # Save previous sequence
                if current_header:
                    sequences[current_header] = "".join(current_sequence)
                
                # Start new sequence
                current_header = line[1:]  # Remove '>'
                current_sequence = []
            else:
                current_sequence.append(line)
        
        # Save last sequence
        if current_header:
            sequences[current_header] = "".join(current_sequence)
    
    return sequences


def write_fasta(sequences, filename):
    """
    Write sequences to FASTA file.
    
    Args:
        sequences (dict): Dictionary of {header: sequence}
        filename (str): Output filename
    """
    with open(filename, 'w') as f:
        for header, sequence in sequences.items():
            f.write(f">{header}\n")
            # Write sequence in lines of 60 characters
            for i in range(0, len(sequence), 60):
                f.write(sequence[i:i+60] + "\n")


def read_fastq(filename):
    """
    Read sequences from FASTQ file.
    
    Args:
        filename (str): Path to FASTQ file
        
    Returns:
        list: List of tuples (header, sequence, quality)
        
    Example FASTQ format:
        @seq1
        ATGCGC
        +
        IIIIII
    """
    records = []
    
    with open(filename, 'r') as f:
        while True:
            header = f.readline().strip()
            if not header:
                break
                
            sequence = f.readline().strip()
            plus = f.readline().strip()
            quality = f.readline().strip()
            
            records.append((header[1:], sequence, quality))
    
    return records


def write_fastq(records, filename):
    """
    Write sequences to FASTQ file.
    
    Args:
        records (list): List of tuples (header, sequence, quality)
        filename (str): Output filename
    """
    with open(filename, 'w') as f:
        for header, sequence, quality in records:
            f.write(f"@{header}\n")
            f.write(f"{sequence}\n")
            f.write("+\n")
            f.write(f"{quality}\n")


def parse_genbank_header(header):
    """
    Parse GenBank-style FASTA header.
    
    Args:
        header (str): GenBank header (e.g., 'gi|123456|ref|NC_000001.1| Homo sapiens')
        
    Returns:
        dict: Parsed header information
    """
    parts = header.split('|')
    if len(parts) >= 4:
        return {
            'gi': parts[1],
            'database': parts[2],
            'accession': parts[3],
            'description': '|'.join(parts[4:]) if len(parts) > 4 else ''
        }
    return {'raw': header}


if __name__ == "__main__":
    # Example: Create a sample FASTA file
    sample_sequences = {
        "gene1 | Sample gene 1": "ATGCGCTAGGCTAA",
        "gene2 | Sample gene 2": "GCTAGCTAGCTAGC",
        "gene3 | Sample gene 3": "ATGATGATGATGAA"
    }
    
    print("Creating sample FASTA file...")
    write_fasta(sample_sequences, "sample.fasta")
    
    print("Reading FASTA file...")
    sequences = read_fasta("sample.fasta")
    
    for header, seq in sequences.items():
        print(f"{header}: {seq}")
