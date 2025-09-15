#!/bin/bash
# Activate virtual environment and run the Jira login script

# Set proxy environment variables
export HTTP_PROXY="http://proxy-nby.gslb.internal.vodafone.co.uk:8080"
export HTTPS_PROXY="http://proxy-nby.gslb.internal.vodafone.co.uk:8080"

# Activate virtual environment
source .venv/Scripts/activate

# Run the script
python login.py

# Deactivate when done
deactivate