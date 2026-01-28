# PPTX Scripts

This directory contains or references the scripts used by the PPTX skill.

## Required Scripts

The following scripts are referenced by the skill and should be available in your working environment:

### Core Workflow Scripts
- `html2pptx.js` - JavaScript library for converting HTML slides to PowerPoint
- `thumbnail.py` - Create visual thumbnail grids of PowerPoint slides
- `rearrange.py` - Duplicate, reorder, and delete slides in presentations
- `inventory.py` - Extract text inventory from presentations  
- `replace.py` - Replace text content in presentations using JSON mapping

### OOXML Scripts (usually in `ooxml/scripts/`)
- `unpack.py` - Unpack .pptx files to XML format
- `pack.py` - Pack XML files back to .pptx format
- `validate.py` - Validate XML structure and content

## Installation Notes

These scripts typically require:
- Python with dependencies like `defusedxml`, `markitdown`
- Node.js with `pptxgenjs`, `playwright`, `sharp`, `react-icons`
- LibreOffice and Poppler utilities

See the main SKILL.md Dependencies section for complete installation instructions.

## Usage

The scripts are called directly from the skill workflows. For example:

```bash
# Create thumbnails
python scripts/thumbnail.py presentation.pptx

# Rearrange slides  
python scripts/rearrange.py template.pptx output.pptx 0,3,5,7

# Extract inventory
python scripts/inventory.py presentation.pptx inventory.json

# Replace content
python scripts/replace.py presentation.pptx replacements.json output.pptx
```

## Script Locations

Depending on your setup, these scripts may be:
- In the skill's scripts directory (if bundled)
- In a shared scripts directory in your workspace
- Part of installed packages or tools
- Referenced from other skill packages

The skill assumes these tools are available in your working environment.