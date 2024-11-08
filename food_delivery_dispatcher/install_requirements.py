import subprocess
import sys

def install_requirements(requirements_file):
    """Install the libraries listed in a requirements.txt file."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("Installation successful.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    requirements_file = "requirements.txt"  # Path to your requirements.txt file
    install_requirements(requirements_file)
