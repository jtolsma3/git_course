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

def choose_llm_model(models):
    candidates = [
        m for m in models
        if ("mistral" in m.lower() or "llama" in m.lower())
    ]
    if not candidates:
        raise RuntimeError("No Mistral or Llama models installed.")
    return random.choice(candidates)
