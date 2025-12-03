import pytest
import subprocess

def test_e2e_valid_expressions():
    result = subprocess.run(["python", "main.py", "5+3"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "8" in result.stdout.strip()

    result = subprocess.run(["python", "main.py", "10-4"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "6" in result.stdout.strip()

def test_e2e_edge_cases():
    result = subprocess.run(["python", "main.py", "5/0"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Error: Division by zero" in result.stderr.strip()

    result = subprocess.run(["python", "main.py", "2+apple"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Error: Invalid characters or malformed expression" in result.stderr.strip()