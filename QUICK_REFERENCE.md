# Python Quick Reference for Genomics

A fast lookup guide for Python fundamentals with genomics examples.

---

## 📝 Data Structures

### Strings (DNA Sequences)
```python
dna = "ATGCGC"
len(dna)              # 6 - length
dna[0]                # 'A' - first character
dna[-1]               # 'C' - last character
dna[0:3]              # 'ATG' - slice (start:end)
dna[::-1]             # 'CGCGTA' - reverse
dna.count('A')        # Count occurrences
'ATG' in dna          # Check if substring exists
dna.find('GC')        # Find position
```

### Lists
```python
genes = ['BRCA1', 'TP53']
genes.append('MYC')   # Add to end
genes[0]              # Access by index
```

### Dictionaries
```python
codon = {'ATG': 'Met', 'TAA': 'Stop'}
codon['ATG']          # Access by key
```

---

See full reference inside the file!
