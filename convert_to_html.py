#!/usr/bin/env python3
"""
Convert The Book of Secret Knowledge (README.md) to HTML
"""

import markdown
from pathlib import Path

def convert_markdown_to_html(input_file, output_file):
    """
    Convert markdown file to HTML with proper styling.
    
    Args:
        input_file (str): Path to the input markdown file
        output_file (str): Path for the output HTML file
    
    Returns:
        None
    
    Raises:
        FileNotFoundError: If the input file does not exist
        IOError: If there are issues reading the input or writing the output
    
    Extensions used:
        - extra: Tables, fenced code blocks, and other extras
        - codehilite: Syntax highlighting for code blocks
        - toc: Table of contents generation
        - sane_lists: Better list handling
        - nl2br: Convert newlines to <br> tags
    """
    
    # Check if input file exists
    if not Path(input_file).exists():
        raise FileNotFoundError(f"Input file '{input_file}' not found")
    
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Configure markdown extensions for better conversion
    md = markdown.Markdown(extensions=[
        'extra',           # Extra features like tables, fenced code blocks
        'codehilite',      # Syntax highlighting
        'toc',             # Table of contents
        'sane_lists',      # Better list handling
        'nl2br',           # Newline to break
    ])
    
    # Convert markdown to HTML
    html_content = md.convert(md_content)
    
    # Create a complete HTML page with styling
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Book of Secret Knowledge</title>
    <style>
        * {{
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
            line-height: 1.6;
            color: #24292e;
            background-color: #ffffff;
            max-width: 980px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }}
        
        h1 {{
            font-size: 2em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }}
        
        h2 {{
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }}
        
        h3 {{
            font-size: 1.25em;
        }}
        
        h4 {{
            font-size: 1em;
        }}
        
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        code {{
            background-color: rgba(27, 31, 35, 0.05);
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 85%;
            margin: 0;
            padding: 0.2em 0.4em;
        }}
        
        pre {{
            background-color: #f6f8fa;
            border-radius: 3px;
            font-size: 85%;
            line-height: 1.45;
            overflow: auto;
            padding: 16px;
        }}
        
        pre code {{
            background-color: transparent;
            border: 0;
            display: inline;
            line-height: inherit;
            margin: 0;
            overflow: visible;
            padding: 0;
            word-wrap: normal;
        }}
        
        blockquote {{
            border-left: 0.25em solid #dfe2e5;
            color: #6a737d;
            margin: 0;
            padding: 0 1em;
        }}
        
        ul, ol {{
            margin-bottom: 16px;
            margin-top: 0;
            padding-left: 2em;
        }}
        
        li + li {{
            margin-top: 0.25em;
        }}
        
        table {{
            border-collapse: collapse;
            border-spacing: 0;
            display: block;
            margin-bottom: 16px;
            margin-top: 0;
            overflow: auto;
            width: 100%;
        }}
        
        table th {{
            font-weight: 600;
        }}
        
        table th, table td {{
            border: 1px solid #dfe2e5;
            padding: 6px 13px;
        }}
        
        table tr {{
            background-color: #fff;
            border-top: 1px solid #c6cbd1;
        }}
        
        table tr:nth-child(2n) {{
            background-color: #f6f8fa;
        }}
        
        img {{
            max-width: 100%;
            height: auto;
        }}
        
        hr {{
            background-color: #e1e4e8;
            border: 0;
            height: 0.25em;
            margin: 24px 0;
            padding: 0;
        }}
        
        p {{
            margin-bottom: 16px;
            margin-top: 0;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        
        .badges {{
            margin: 20px 0;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""
    
    # Write the HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"Successfully converted {input_file} to {output_file}")
    print(f"Output file size: {Path(output_file).stat().st_size} bytes")

if __name__ == "__main__":
    input_file = "README.md"
    output_file = "the-book-of-secret-knowledge.html"
    
    try:
        convert_markdown_to_html(input_file, output_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure README.md exists in the current directory.")
        exit(1)
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        exit(1)
