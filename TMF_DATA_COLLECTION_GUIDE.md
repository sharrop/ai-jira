# TMF Rules Files Data Collection Guide

Since you can browse the repository at `https://github.com/tmforum-rand/OAS_Open_API_And_Data_Model/tree/v5.0.0-dev/apis`, here's a systematic approach to collect the data:

## Quick Start Instructions

### Step 1: Open the Repository
1. Go to: https://github.com/tmforum-rand/OAS_Open_API_And_Data_Model/tree/v5.0.0-dev/apis
2. You should see a list of TMF directories (TMF620_Product_Catalog, TMF621_Trouble_Ticket, etc.)

### Step 2: For Each Directory
1. Click on a TMF directory (e.g., TMF620_Product_Catalog)
2. Look for any file ending in `.rules.yaml`
3. If you find one, click on it
4. Once in the file view, click the "History" button (clock icon) in the top-right area of the file
5. Note the most recent commit information:
   - **Date**: When it was last modified
   - **Author**: Who made the last change  
   - **Message**: What the commit message says
   - **SHA**: The short commit hash (first 7 characters)

### Step 3: Record the Information
Open the generated CSV template (`tmf_rules_manual_template.csv`) and fill in:
- Mark "FILE NOT FOUND" in the notes column if no .rules.yaml file exists
- Fill in the commit information for files that do exist

## Browser Automation Script

If you want to semi-automate this process, you can use this JavaScript code in your browser's developer console:

```javascript
// Run this on the main apis directory page
// https://github.com/tmforum-rand/OAS_Open_API_And_Data_Model/tree/v5.0.0-dev/apis

console.log("TMF Directories found:");
const directories = [];
document.querySelectorAll('a[href*="/tree/v5.0.0-dev/apis/TMF"]').forEach(link => {
    const dirName = link.href.split('/').pop();
    if (dirName.startsWith('TMF')) {
        directories.push(dirName);
        console.log(dirName);
    }
});

console.log(`Total: ${directories.length} directories`);
console.log("Copy this list and check each directory manually for .rules.yaml files");
```

## Expected File Patterns

Based on TMF standards, look for files like:
- `TMF620_Product_Catalog.rules.yaml`
- `TMF621_Trouble_Ticket.rules.yaml`
- `rules.yaml`
- `validation.rules.yaml`
- Any file ending in `.rules.yaml`

## CSV Template Headers

The CSV template has these columns:
- **directory**: The TMF directory name (e.g., TMF620_Product_Catalog)
- **filename**: The actual filename of the rules file
- **file_path**: Full path (apis/TMF620_Product_Catalog/filename.rules.yaml)
- **last_commit_date**: ISO date format (YYYY-MM-DDTHH:MM:SSZ)
- **last_commit_message**: The commit message
- **last_author**: Name of the person who made the last commit
- **commit_sha**: Short commit hash (7 characters)
- **notes**: Any additional notes (use "FILE NOT FOUND" if no rules file exists)

## Time-Saving Tips

1. **Use browser tabs**: Open multiple TMF directories in separate tabs
2. **Use Ctrl+F**: Search for "rules.yaml" on directory pages
3. **Copy-paste efficiently**: Select and copy commit info directly from GitHub
4. **Work systematically**: Go through directories alphabetically
5. **Save frequently**: Update the CSV as you go, don't wait until the end

## Alternative: GitHub Search

You can also use GitHub's search to find rules files:
1. Go to the repository main page
2. Use the search box and enter: `filename:rules.yaml`
3. This will show all rules.yaml files in the repository
4. Filter by the v5.0.0-dev branch if possible

## Validation

After completing the CSV:
- Check that you've covered all TMF directories visible in the apis folder
- Verify date formats are consistent
- Ensure file paths are correct
- Count total files found vs total directories checked

Good luck with the data collection!