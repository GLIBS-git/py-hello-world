# Check if pip installed 
pip --version

# Check if venv is installed
python3 -m venv --help

# Install venv if not installed
sudo apt install python3-venv

# Check if venv is activated
python3 -c "import sys; print(sys.executable)"

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Deactivate virtual environment
deactivate

# Install pip packages in virtual environment or globally (on Windows)
pip install requests

# Check if pip packages are installed
pip list
pip show requests









