@echo off
REM Run JIRA Issue Quality Check and Generate Reports
REM This script runs the quality check and creates both plain text and markdown reports

echo 🚀 Starting JIRA Issue Quality Check...
echo ==================================================

REM Set proxy environment variables
set HTTP_PROXY=http://proxy-nby.gslb.internal.vodafone.co.uk:8080
set HTTPS_PROXY=http://proxy-nby.gslb.internal.vodafone.co.uk:8080

REM Activate virtual environment
echo 📦 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Run the quality check and save to report.txt
echo 🔍 Running JIRA quality check...
py check_issues.py > report.txt 2>&1

REM Check if the report was generated successfully
if exist "report.txt" (
    echo ✅ Quality check completed successfully!
    echo 📄 Report saved to: report.txt
    
    REM Convert to markdown formats
    echo 🔄 Converting to markdown formats...
    
    REM Basic markdown conversion
    py convert_to_markdown.py
    
    REM Enhanced markdown conversion
    py create_enhanced_report.py
    
    echo ✅ Conversion completed!
    echo 📝 Available reports:
    echo    - report.txt (Plain text)
    echo    - report.md (Basic markdown)
    echo    - report_enhanced.md (Enhanced markdown)
    
) else (
    echo ❌ Error: Quality check failed. No report generated.
    echo Check the output above for error details.
    exit /b 1
)

REM Deactivate virtual environment
call deactivate

echo.
echo 🎉 All reports generated successfully!
echo 💡 Tip: Open report_enhanced.md in VS Code for the best viewing experience.

pause