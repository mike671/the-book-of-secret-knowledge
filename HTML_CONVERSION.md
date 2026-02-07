# HTML Conversion

This repository includes a tool to convert "The Book of Secret Knowledge" from Markdown to HTML format.

## Quick Start

The HTML version of the book has already been generated and is available as:
- **`the-book-of-secret-knowledge.html`** - The complete book in a single HTML file

Simply open this file in any web browser to view the book offline.

## Regenerating the HTML

If you make changes to the README.md and want to regenerate the HTML file:

### Prerequisites

- Python 3.6 or higher
- The `markdown` Python package

### Installation

Install the required Python package:

```bash
pip install markdown
```

### Usage

Run the conversion script:

```bash
python3 convert_to_html.py
```

This will:
1. Read the `README.md` file
2. Convert it to HTML with proper styling
3. Generate `the-book-of-secret-knowledge.html`

## Features

The generated HTML file includes:

- **GitHub-style formatting** - Clean, readable design similar to GitHub's markdown renderer
- **Syntax highlighting** - Code blocks with proper highlighting
- **Responsive design** - Works on desktop and mobile devices
- **Table of contents** - All section links are preserved and functional
- **Embedded styles** - No external dependencies, works offline
- **Images and links** - All links and images from the markdown are preserved

## File Structure

- `convert_to_html.py` - The conversion script
- `README.md` - The source markdown file
- `the-book-of-secret-knowledge.html` - The generated HTML output
- `HTML_CONVERSION.md` - This documentation file

## Customization

To customize the HTML output, edit the `convert_to_html.py` file:

- Modify the CSS in the `html_template` variable to change styling
- Adjust the `markdown.Markdown()` extensions to enable/disable features
- Change the output filename by modifying the `output_file` variable

## Notes

- The HTML file is self-contained and can be opened directly in any web browser
- All styles are embedded in the HTML file for offline viewing
- The file size is approximately 367 KB
