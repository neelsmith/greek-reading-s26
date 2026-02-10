#!/usr/bin/env python3
"""
Format text file with alternating numeric and text lines into Quarto columns.
Ignores numeric lines and wraps text lines in the specified column structure.
"""

def is_numeric_line(line):
    """Check if a line contains only a number."""
    return line.strip().isdigit()

def format_text_line(text, linenum):
    """Format a text line into Quarto columns structure."""
    return f""":::: {{.columns}}

::: {{.column width="60%"}}
`{linenum}` {text}
:::

::: {{.column width="10%"}}
:::

::: {{.column width="20%" .sidenote}}
:::

::::
"""

def format_file(input_file, output_file):
    """Read input file and format text lines into output file."""
    formatted_lines = []
    
    with open(input_file, 'r', encoding='utf-8', errors='surrogateescape') as f:
        for linenum, line in enumerate(f, start=2174):
            line = line.rstrip('\n\r')
            num = int(linenum / 2)
            # Skip empty lines and numeric lines
            if line and not is_numeric_line(line):
                formatted_lines.append(format_text_line(line, num))
    
    # Write formatted output with explicit UTF-8 encoding and newline handling
    with open(output_file, 'w', encoding='utf-8', errors='surrogateescape', newline='') as f:
        f.write('\n'.join(formatted_lines))
    
    print(f"Formatted {len(formatted_lines)} text lines from {input_file} to {output_file}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python format_text.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    format_file(input_file, output_file)
