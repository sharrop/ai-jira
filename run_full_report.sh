#!/bin/bash
# Run JIRA Issue Quality Check and Generate Reports
# This script runs the quality check and creates both plain text and markdown reports

echo "🚀 Starting JIRA Issue Quality Check..."
echo "=" * 50

# Set proxy environment variables
export HTTP_PROXY="http://proxy-nby.gslb.internal.vodafone.co.uk:8080"
export HTTPS_PROXY="http://proxy-nby.gslb.internal.vodafone.co.uk:8080"

# Activate virtual environment
echo "📦 Activating virtual environment..."
source .venv/Scripts/activate

# Run the quality check and save to report.txt
echo "🔍 Running JIRA quality check..."
py check_issues.py > report.txt 2>&1

# Check if the report was generated successfully
if [ -f "report.txt" ]; then
    echo "✅ Quality check completed successfully!"
    echo "📄 Report saved to: report.txt"
    
    # Get file size
    size=$(wc -c < report.txt)
    echo "📊 Report size: $size bytes"
    
    # Convert to markdown formats
    echo "🔄 Converting to markdown formats..."
    
    # Basic markdown conversion
    py convert_to_markdown.py
    
    # Enhanced markdown conversion
    py create_enhanced_report.py
    
    echo "✅ Conversion completed!"
    echo "📝 Available reports:"
    echo "   - report.txt (Plain text)"
    echo "   - report.md (Basic markdown)"
    echo "   - report_enhanced.md (Enhanced markdown)"
    
    # Show file sizes
    if [ -f "report.md" ]; then
        md_size=$(wc -c < report.md)
        echo "   - report.md size: $md_size bytes"
    fi
    
    if [ -f "report_enhanced.md" ]; then
        enhanced_size=$(wc -c < report_enhanced.md)
        echo "   - report_enhanced.md size: $enhanced_size bytes"
    fi
    
else
    echo "❌ Error: Quality check failed. No report generated."
    echo "Check the output above for error details."
    exit 1
fi

# Deactivate virtual environment
deactivate

echo ""
echo "🎉 All reports generated successfully!"
echo "💡 Tip: Open report_enhanced.md in VS Code for the best viewing experience."