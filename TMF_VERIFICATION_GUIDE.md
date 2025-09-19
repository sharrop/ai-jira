
# TMF Repository Verification Guide

## Step 1: Verify Repository Access
1. Go to: https://github.com/tmforum-rand/OAS_Open_API_And_Data_Model
2. Check if you can access it (you might need to be logged in)
3. If you can't access it, try these alternatives:
   - https://github.com/tmforum/OAS_Open_API_And_Data_Model
   - https://github.com/TMForum/OAS_Open_API_And_Data_Model
   - Search for "tmforum openapi" on GitHub

## Step 2: Navigate to the APIs Directory
1. Once you find the repository, go to the branch: v5.0.0-dev
2. Navigate to the "apis" directory
3. You should see directories like TMF620_Product_Catalog, TMF621_Trouble_Ticket, etc.

## Step 3: Check for Rules Files
1. Go into each TMF directory (e.g., TMF620_Product_Catalog)
2. Look for files ending in ".rules.yaml"
3. Note the exact filename

## Step 4: Get Commit Information
For each rules file you find:
1. Click on the file in GitHub
2. Click "History" or "Blame" button
3. Note the last commit information:
   - Date
   - Author
   - Commit message
   - Commit SHA

## Step 5: Fill the CSV Template
Use the generated CSV template and fill in:
- Mark files that don't exist by adding "FILE NOT FOUND" in notes
- Fill commit information for files that do exist
- Save the completed CSV

## Alternative: Use GitHub CLI
If you have GitHub CLI installed:
```bash
# List contents of apis directory
gh api repos/tmforum-rand/OAS_Open_API_And_Data_Model/contents/apis?ref=v5.0.0-dev

# Get commit info for a specific file
gh api "repos/tmforum-rand/OAS_Open_API_And_Data_Model/commits?path=apis/TMF620_Product_Catalog/FILENAME.rules.yaml&per_page=1"
```

## Alternative: Clone and Use Git
If the repository is accessible for cloning:
```bash
git clone -b v5.0.0-dev https://github.com/tmforum-rand/OAS_Open_API_And_Data_Model.git
cd OAS_Open_API_And_Data_Model/apis
find . -name "*.rules.yaml" -exec git log -1 --format="%H,%ai,%an,%s" {} \; > ../rules_commits.csv
```
