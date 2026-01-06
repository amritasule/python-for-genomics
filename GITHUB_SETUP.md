# GitHub Setup Instructions

## Step 1: Initialize Git Repository

```bash
cd /home/claude/python-for-genomics
git init
```

## Step 2: Add All Files

```bash
git add .
```

## Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: Python for Genomics toolkit

- Added DNA manipulation tools (dna_tools.py)
- Added sequence analysis functions (sequence_analysis.py)  
- Added FASTA/FASTQ file parsers (file_parsers.py)
- Added example scripts demonstrating usage
- Added sample data and comprehensive documentation"
```

## Step 4: Create GitHub Repository

1. Go to https://github.com
2. Click the "+" in the top right
3. Select "New repository"
4. Name it: `python-for-genomics`
5. Description: "Python toolkit for genomic data analysis and bioinformatics"
6. Choose Public or Private
7. **DO NOT** initialize with README (we already have one)
8. Click "Create repository"

## Step 5: Connect to GitHub

```bash
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/python-for-genomics.git

# For newer GitHub accounts, the default branch is 'main'
git branch -M main
```

## Step 6: Push to GitHub

```bash
git push -u origin main
```

If prompted for credentials:
- Username: Your GitHub username
- Password: Use a Personal Access Token (not your password)

### Creating a Personal Access Token

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name: "python-for-genomics"
4. Select scopes: Check "repo" (full control of private repositories)
5. Click "Generate token"
6. **COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
7. Use this token as your password when pushing

## Step 7: Verify

Go to your GitHub repository URL and you should see all your files!

## Future Updates

After making changes:

```bash
# Check what changed
git status

# Add changes
git add .

# Commit with message
git commit -m "Add new feature or fix bug"

# Push to GitHub
git push
```

## Alternative: Using SSH

If you prefer SSH (recommended for frequent use):

1. Generate SSH key:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

2. Add to GitHub:
   - Copy the public key: `cat ~/.ssh/id_ed25519.pub`
   - Go to GitHub → Settings → SSH and GPG keys → New SSH key
   - Paste the key

3. Change remote URL:
```bash
git remote set-url origin git@github.com:YOUR_USERNAME/python-for-genomics.git
```

4. Push:
```bash
git push -u origin main
```

## Common Issues

**Issue**: "Repository not found" or "Permission denied"
**Solution**: Make sure you created the repository on GitHub and replaced YOUR_USERNAME with your actual username

**Issue**: "Authentication failed"
**Solution**: Make sure you're using a Personal Access Token, not your password

**Issue**: "src refspec main does not match any"
**Solution**: Make sure you've made at least one commit before pushing

## Repository Features to Enable

After pushing, consider enabling:
1. **GitHub Pages** - Host documentation
2. **Issues** - Track bugs and features
3. **Projects** - Organize development
4. **Actions** - Automate testing

Enjoy your new GitHub repository! 🎉
