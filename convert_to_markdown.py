"""
Convert existing report.txt to markdown format

This script reads the report.txt file and converts it to a properly formatted
markdown report that's easier to read and can be viewed in any markdown viewer.
"""

import sys
import re
from datetime import datetime
from markdown_reporter import convert_console_output_to_markdown


def main():
    """Convert report.txt to markdown format"""
    
    # Default input and output files
    input_file = "report.txt"
    output_file = "report.md"
    
    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    try:
        # Read the existing report
        print(f"Reading report from: {input_file}")
        with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
            console_content = f.read()
        
        print(f"Converting to markdown format...")
        
        # Convert to markdown
        markdown_content = convert_console_output_to_markdown(console_content)
        
        # Write the markdown report
        print(f"Writing markdown report to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Successfully converted report to markdown!")
        print(f"📄 Input: {input_file}")
        print(f"📝 Output: {output_file}")
        
        # Show file sizes
        import os
        input_size = os.path.getsize(input_file) if os.path.exists(input_file) else 0
        output_size = os.path.getsize(output_file) if os.path.exists(output_file) else 0
        print(f"📊 Input size: {input_size:,} bytes")
        print(f"📊 Output size: {output_size:,} bytes")
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find input file: {input_file}")
        print(f"Make sure the report file exists and try again.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error converting report: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()