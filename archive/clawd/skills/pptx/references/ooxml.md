# OOXML Editing Workflow

## Overview

When editing slides in an existing PowerPoint presentation, you need to work with the raw Office Open XML (OOXML) format. This involves unpacking the .pptx file, editing the XML content, and repacking it.

## Complete Workflow

### 1. Unpack the presentation
```bash
python ooxml/scripts/unpack.py <office_file> <output_dir>
```

**Note**: The unpack.py script is located at `skills/pptx/ooxml/scripts/unpack.py` relative to the project root. If the script doesn't exist at this path, use `find . -name "unpack.py"` to locate it.

### 2. Understanding File Structures

#### Key file structures
* `ppt/presentation.xml` - Main presentation metadata and slide references
* `ppt/slides/slide{N}.xml` - Individual slide contents (slide1.xml, slide2.xml, etc.)
* `ppt/notesSlides/notesSlide{N}.xml` - Speaker notes for each slide
* `ppt/comments/modernComment_*.xml` - Comments for specific slides
* `ppt/slideLayouts/` - Layout templates for slides
* `ppt/slideMasters/` - Master slide templates
* `ppt/theme/` - Theme and styling information
* `ppt/media/` - Images and other media files

#### Typography and color extraction
**When given an example design to emulate**: Always analyze the presentation's typography and colors first using the methods below:
1. **Read theme file**: Check `ppt/theme/theme1.xml` for colors (`<a:clrScheme>`) and fonts (`<a:fontScheme>`)
2. **Sample slide content**: Examine `ppt/slides/slide1.xml` for actual font usage (`<a:rPr>`) and colors
3. **Search for patterns**: Use grep to find color (`<a:solidFill>`, `<a:srgbClr>`) and font references across all XML files

### 3. Edit the XML files

Edit the XML files (primarily `ppt/slides/slide{N}.xml` and related files) based on your requirements.

**Key XML elements for slide content**:
- `<p:sp>` - Shape elements
- `<a:t>` - Text content
- `<a:rPr>` - Text run properties (formatting)
- `<a:pPr>` - Paragraph properties
- `<p:txBody>` - Text body container

### 4. Validate Changes (CRITICAL)

**CRITICAL**: Validate immediately after each edit and fix any validation errors before proceeding:
```bash
python ooxml/scripts/validate.py <dir> --original <file>
```

This step is essential to ensure the XML remains valid and the presentation will open correctly.

### 5. Pack the final presentation
```bash
python ooxml/scripts/pack.py <input_directory> <office_file>
```

## Best Practices

1. **Always validate after each major change** - Don't wait until the end
2. **Keep backups** - Make copies before starting major edits
3. **Test with small changes first** - Verify your workflow on simple edits
4. **Understand the XML structure** - Study the existing content before making changes
5. **Be careful with namespaces** - Maintain proper XML namespace declarations

## Common XML Patterns

### Text Content
```xml
<a:t>Your text content here</a:t>
```

### Bold Text
```xml
<a:r>
  <a:rPr b="1"/>
  <a:t>Bold text</a:t>
</a:r>
```

### Font Properties
```xml
<a:rPr>
  <a:latin typeface="Arial"/>
  <a:sz val="2000"/>  <!-- Font size in hundredths of a point -->
</a:rPr>
```

### Colors
```xml
<!-- Solid RGB color -->
<a:solidFill>
  <a:srgbClr val="FF0000"/>  <!-- Red -->
</a:solidFill>

<!-- Theme color -->
<a:solidFill>
  <a:schemeClr val="accent1"/>
</a:solidFill>
```

## Troubleshooting

**File won't open after editing**: Usually indicates invalid XML. Run validation script and fix reported errors.

**Text formatting lost**: Check that `<a:rPr>` elements are properly structured and closed.

**Slides appear blank**: Verify that shape and text body elements maintain proper hierarchy.

**Images missing**: Ensure media files are referenced correctly in relationships and that file paths match.