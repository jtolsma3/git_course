import subprocess
import random

def list_ollama_models():
    result = subprocess.run(
        ["ollama","list"],
        capture_output = True,
        text = True,
        check = True
    )

    lines = result.stdout.strip().splitlines()[1:]
    models = [line.split()[0] for line in lines]
    return models
