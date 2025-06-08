import subprocess
import sys

# List of math operation scripts to run in order
scripts = ["add.py", "substract.py", "multiply.py", "divide.py"]

for script in scripts:
    try:
        result = subprocess.run(
            [sys.executable, script],
            capture_output=True,
            text=True,
            check=False
        )
        print(result.stdout, end='')
        if result.stderr:
            print("Errors:", result.stderr)
    except Exception as e:
        print(f"Error running {script}: {e}")
    print("\n\n", end='')  # Two line feeds between outputs