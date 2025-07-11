# in modules/code_analyzer.py
import subprocess
import json

def analyze_file(filepath):
    """
    Runs pylint on a file and returns a list of issues.
    This is a simplified example; a real-world tool would be more robust.
    """
    print(f"Analyzing {filepath}...")
    try:
        # Run pylint with JSON output
        command = [
            "pylint",
            "--output-format=json",
            filepath
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        # Pylint exits with a non-zero status for issues, so we check stdout
        if result.stdout:
            return json.loads(result.stdout)
        return []
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error analyzing file {filepath}: {e}")
        return []