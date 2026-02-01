import subprocess
import random
import requests

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

def ollama_generate(model,prompt):
    resp = requests.post("http://localhost:11434/api/generate",
        json = {
            "model":model,
            "prompt":prompt,
            "stream":False,
        },
        timeout = 30
    )
    resp.raise_for_status()
    return resp.json()["response"]

def run_joke_pipeline():
    prompt = """
    Please tell me a short, clever joke involving computer programming.
    Please do not explain the joke afterwards and assume that your audience 
    is savvy about computer programming languages, technologies, and topics.
    """
    models = list_ollama_models()
    model = choose_llm_model(models)
    joke = ollama_generate(model,prompt)
    return model,joke
