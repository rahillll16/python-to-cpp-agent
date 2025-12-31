from core.prompts import system_prompt, coder_prompt
from core.models import CLIENTS

def generate_code(model: str, python_code: str, plan: str, language: str) -> str:
    client = CLIENTS[model]

    response = client.chat.completions.create(
        model=model,
        reasoning_effort="high" if "gpt" in model else None,
        messages=[
            {"role": "system", "content": system_prompt(language)},
            {"role": "user", "content": coder_prompt(python_code, plan, language)}
        ]
    )

    code = response.choices[0].message.content
    return code.replace("```cpp", "").replace("```", "").strip()
