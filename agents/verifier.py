from core.prompts import verifier_prompt
from core.models import CLIENTS

def verify(model: str, code: str, language: str) -> str:
    client = CLIENTS[model]
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": verifier_prompt(code, language)}]
    )
    return response.choices[0].message.content.strip()
