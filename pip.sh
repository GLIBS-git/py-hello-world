# Check if pip installed 
pip --version

# Check if venv is installed
python3 -m venv --help

# Install venv if not installed
sudo apt install python3-venv

# Check if venv is activated
python3 -c "import sys; print(sys.executable)"

# Activate venv
source .venv/bin/activate

# Deactivate venv
deactivate

# Install packages in venv
pip install requests

# Check if packages are installed
pip list
pip show requests









