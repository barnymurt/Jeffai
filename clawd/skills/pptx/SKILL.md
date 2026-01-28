---
name: pptx
description: "Presentation creation, editing, and analysis. When Claude needs to work with presentations (.pptx files) for: (1) Creating new presentations, (2) Modifying or editing content, (3) Working with layouts, (4) Adding comments or speaker notes, or any other presentation tasks"
---

# PPTX creation, editing, and analysis

## Overview

A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx file is essentially a ZIP archive containing XML files and other resources that you can read or edit. You have different tools and workflows available for different tasks.

## Workflow Decision Tree

Choose your approach based on the task:

1. **Reading/analyzing content** → Text extraction or raw XML access
2. **Creating new presentation (no template)** → HTML2PPTX workflow  
3. **Creating new presentation (with template)** → Template duplication workflow
4. **Editing existing presentation** → OOXML editing workflow
5. **Visual analysis** → Thumbnail grids or slide-to-image conversion

## Reading and Analyzing Content

### Text extraction
If you just need to read the text contents of a presentation, convert to markdown:
```bash
python -m markitdown path-to-file.pptx
```

### Raw XML access
For comments, speaker notes, slide layouts, animations, design elements, and complex formatting, unpack and read raw XML:
```bash
python ooxml/scripts/unpack.py <office_file> <output_dir>
```

**Key file structures**:
- `ppt/presentation.xml` - Main presentation metadata and slide references
- `ppt/slides/slide{N}.xml` - Individual slide contents 
- `ppt/notesSlides/notesSlide{N}.xml` - Speaker notes
- `ppt/comments/modernComment_*.xml` - Comments
- `ppt/slideLayouts/` - Layout templates
- `ppt/theme/` - Theme and styling information
- `ppt/media/` - Images and other media files

## Creating New Presentations Without Templates

Use the **html2pptx** workflow for new presentations from scratch.

### Design Principles

**CRITICAL**: Before creating any presentation, analyze the content and choose appropriate design elements:
1. **Consider the subject matter**: What tone, industry, or mood does it suggest?
2. **Check for branding**: Consider company/organization brand colors
3. **Match palette to content**: Select colors that reflect the subject
4. **State your approach**: Explain design choices before writing code

**Requirements**:
- ✅ State your content-informed design approach BEFORE writing code
- ✅ Use web-safe fonts only: Arial, Helvetica, Times New Roman, Georgia, Courier New, Verdana, Tahoma, Trebuchet MS, Impact
- ✅ Create clear visual hierarchy through size, weight, and color
- ✅ Ensure readability: strong contrast, appropriately sized text, clean alignment

### Workflow
1. **MANDATORY**: Read [`html2pptx.md`](references/html2pptx.md) completely first
2. Create HTML files for each slide with proper dimensions (720pt × 405pt for 16:9)
3. Create and run JavaScript file using html2pptx library to convert and save
4. **Visual validation**: Generate thumbnails and inspect for layout issues

## Creating New Presentations Using Templates

When following an existing template's design:

### Workflow
1. **Extract and analyze template**:
   - Extract text: `python -m markitdown template.pptx`
   - Create thumbnails: `python scripts/thumbnail.py template.pptx`
   - Analyze and create template inventory
2. **Create presentation outline** based on template inventory
3. **Duplicate and reorder slides** using `rearrange.py`
4. **Extract text inventory** using `inventory.py` 
5. **Generate replacement text** and save to JSON
6. **Apply replacements** using `replace.py`

For detailed workflow: See [Template Workflow](references/template-workflow.md)

## Editing Existing Presentations

For modifying existing .pptx files, work with raw OOXML format:

### Workflow
1. **MANDATORY**: Read [`ooxml.md`](references/ooxml.md) completely first
2. Unpack: `python ooxml/scripts/unpack.py <file> <output_dir>`
3. Edit XML files (primarily `ppt/slides/slide{N}.xml`)
4. **CRITICAL**: Validate after each edit: `python ooxml/scripts/validate.py <dir> --original <file>`
5. Pack: `python ooxml/scripts/pack.py <input_directory> <office_file>`

## Visual Analysis Tools

### Creating Thumbnail Grids
```bash
python scripts/thumbnail.py template.pptx [output_prefix]
# Options: --cols 4 (3-6 columns), custom output directory
```

### Converting Slides to Images
1. Convert to PDF: `soffice --headless --convert-to pdf template.pptx`
2. Convert PDF to images: `pdftoppm -jpeg -r 150 template.pdf slide`

## Code Style Guidelines

When generating code for PPTX operations:
- Write concise code
- Avoid verbose variable names and redundant operations
- Avoid unnecessary print statements

## Dependencies

Required tools (should already be installed):
- **markitdown**: `pip install "markitdown[pptx]"`
- **pptxgenjs**: `npm install -g pptxgenjs` 
- **playwright**: `npm install -g playwright`
- **react-icons**: `npm install -g react-icons react react-dom`
- **sharp**: `npm install -g sharp`
- **LibreOffice**: `sudo apt-get install libreoffice`
- **Poppler**: `sudo apt-get install poppler-utils`
- **defusedxml**: `pip install defusedxml`