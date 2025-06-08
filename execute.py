import subprocess
import sys
import os

# List of math operation scripts to run in order
math_folder = "math"
scripts = sorted(
    f for f in os.listdir(math_folder)
    if f.endswith('.py') and os.path.isfile(os.path.join(math_folder, f))
)

for script in scripts:
    script_path = os.path.join(math_folder, script)
    try:
        result = subprocess.run(
            [sys.executable, script_path],
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